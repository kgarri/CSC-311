import io 
import os.path 
import heapq
#there is  some edits between this code and the code from https://github.com/asioson/huffman/blob/main/huffman.py as it did somethings that didn't makesense 
# and we added the node information to better match up how most trees are stored through linked nodes 
# additionally added commments for context and edited certain sections of the code to improve some effciency and to make the code more readable than the orginal

class node: # this is used to build a tree that can be used to make a huffman tree
    def __init__(self, freq , symbol):
        self.freq = freq
        self.symbol = symbol
        self.left = None 
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

class huff: 
    
    def __init__(self):
        self.code = {} #this stores the code that will later be used in the decompression proces
        self.data = 0  #this stores the actual data that is encoded
        self.dataMask = 0x80  # the starting out value of the dataMask is hex 80
        self.freq = [0] * 256 # this stores the frequncy in an array of 256 possible characters
    def saveBit(self, f,b): 
        if b == 1 : 
            self.data = self.data | self.dataMask #using bit wise or used to combine the data with the dataMask
        if self.dataMask != 0x01 :
            self.dataMask = self.dataMask >> 1 #shifts the bits of the bit mask to the write
        else: 
            f.write(self.data.to_bytes(1,"little")) #writes the value to the file as a little bytes, 1 byte object
            self.dataMask = 0x80 #resets dataMask
            self.data = 0 #resets data

    def genCode(self, t, b): #t repersents the tree and b repersents the byte array repersenation
        if t == None:
            return
        if t.symbol != -1:
            self.code[t.symbol] = b[:]
        self.genCode(t.left, b + [0])
        self.genCode(t.right, b + [1])

    def makeHuff(self,arr): #makes the huffman tree by utilizing the node class with the left and right child nodes
        heapq.heapify(arr) # pushes the arr onto the heap and makes it a queue
        while len(arr) >1:
            left = heapq.heappop(arr)#removes first element at the top of the queue
            right = heapq.heappop(arr)
            c = node(freq= left.freq + right.freq, symbol = -1) # makes new hufffman node
            c.left = left 
            c.right = right
            heapq.heappush(arr,c)
        return arr[0]

    def genFreqTable(self, ifname): 
        self.freq = [0] * 256 #makes a 256 length array, to accomidate 256 unique byte signatures
        with io.open(ifname,'rb') as f:
            b = f.read(1)
            while b!=b"": #going through the file byte by byte, saving the data as needed
                self.freq[int.from_bytes(b,"little")] += 1 #counting the freq of that byte in an array where the index is the unique byte
                b = f.read(1)
        f.close()
        treeList = []
        for i in range(256): #256 unique bytes iterating over the frequncy array
            if self.freq[i]>0:
                treeList.append(node(self.freq[i], i )) #adds new node to the tree list
        return treeList

    def encodeFile(self, code, ifsize, ifname, ofname): # code: array of huffman codes, ifsize : the in file size, ifname: in file name, ofname: out file name
        ofile = io.open(ofname,'wb') #opening the output file in bytes mode
        ofile.write(ifsize.to_bytes(4,"little")) #size of the original file in 4 bytes
        for i in range(256) : 
            ofile.write(self.freq[i].to_bytes(4,"little")) #the freq of occurance of each byte in the file 
        with io.open(ifname,'rb') as ifile : #the actual encodeing portion of the file 
            b = ifile.read(1)
            while b != b"" :
                for x in code[int.from_bytes(b,"little")] :
                    self.saveBit(ofile, x)
                b = ifile.read(1)
        ifile.close()
        while self.dataMask != 0x80 :
            self.saveBit(ofile,0)
        ofile.close()

    def compress(self, ifname, ofname) : # the compression steps
        ifsize = os.path.getsize(ifname) #first get the size of the file
        huffTree = self.makeHuff(self.genFreqTable(ifname)) #build a huffman tree
        self.code.clear() #ensure that nothing remains in the code cache
        self.genCode(huffTree,[]) # generate the actual unique codes of the huffman tree
        self.encodeFile(self.code, ifsize, ifname, ofname) #encode the file including a header that is later decoded
        ofsize = os.path.getsize(ofname) #get the output size of the file 
        print('compressed = {:d}, uncompressed = {:d}'.format(ofsize,ifsize)) #pring the compressed and uncompressed file sizes


    def readBit(self, f):
        if self.data == -1:
            self.data = f.read(1)
            if self.data == b"": #if end of file reteurn -1
                return -1
            self.data = int.from_bytes(self.data,"little") #encodes bytes using little-endian format most signifigant bit on the left
            self.dataMask = 0x80 #resets the dataMask
        if self.data == b"": #if there is no data leave
            return -1

        bit = 1 if ((self.data & self.dataMask != 0)) else  0 #using bitwise & to determine if the bit is a 1 or zero
        if self.dataMask != 0x01: #making sure to decerment the dataMask
            self.dataMask = self.dataMask  >>1
        else:
            self.data = f.read(1) #reading another bit of info
            if self.data ==b"": #if there is no data return the bit
                return bit
            self.data = int.from_bytes(self.data,"little") #encode the data as little-endian
            self.dataMask = 0x80 #reset dataMask
        return bit #return the bit

    def loadFreqTable(self, ifname): # loads the freqTable and reconstructs the huffman tree
        self.freq = [0] * 256
        with io.open(ifname, 'rb') as f:
            b = f.read(4)
            for i in range(256):
                b = f.read(4)
                self.freq[i] = int.from_bytes(b, "little")
        f.close()
        treeList =[]
        for i in range(256):
            if self.freq[i]>0:
                treeList.append(node(self.freq[i],i))
        return treeList

    def decodeFile(self, huffTree, ifname, ofname) :
        ofile = io.open(ofname,'wb')
        with io.open(ifname,'rb') as ifile :
            fsize = int.from_bytes(ifile.read(4),"little")
            count = 0
            for i in range(256) : b = ifile.read(4)
            self.data = -1
            bit = self.readBit(ifile)
            ht = huffTree
            while bit != -1 :
                if bit == 0 :
                    ht = ht.left
                else :
                    ht = ht.right
                if ht.left is None and ht.right is None :
                    if count < fsize :
                        ofile.write(ht.symbol.to_bytes(1,"little"))
                        count += 1
                    ht = huffTree
                bit = self.readBit(ifile)
        ifile.close()
        ofile.close()

    def decompress(self, ifname, ofname) :
        huffTree = self.makeHuff(self.loadFreqTable(ifname))
        self.decodeFile(huffTree, ifname, ofname)
        ifsize = os.path.getsize(ifname)
        ofsize = os.path.getsize(ofname)
        print('compressed = {:d}, uncompressed = {:d}'.format(ifsize,ofsize))
