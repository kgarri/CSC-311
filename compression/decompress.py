from huffman import huff
import sys
import os
# this is a utility file for decompressing a huff encoded file this is again done by taking in sy arguments opening the file and creating a new output file with .orig at the end
def main() :
    if len(sys.argv) != 2 :
        print('usage: ' + sys.argv[0] + ' file.huff')
    else :
        ifname = sys.argv[1]
        if not os.path.exists(ifname) :
            print('error: file "' + ifname + '" not found.')
            return 1
        if ifname[-5:] != '.huff' :
            print('error: file "' + ifname + '" is not huff compressed.')
            return 1
        ofname = ifname[:-5] + '.orig'
        if os.path.exists(ofname) :
            print('error: file "' + ofname + '" exists.')
            return 1
        h = huff()
        h.decompress(ifname, ofname)
    return 0


if __name__ == '__main__' :
    sys.exit(main())
