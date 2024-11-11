from huffman import huff
import sys
import os
# this is used to execute the compression algorithim by taking in a system arg and editing the filename to end in huff
def main() :
    if len(sys.argv) != 2 :
        print('usage: ' + sys.argv[0] + ' file')
    else :
        ifname = sys.argv[1]
        if not os.path.exists(ifname) :
            print('error: file "' + ifname + '" not found.')
            return 1
        if ifname[-5:] == '.huff' :
            print('error: file "' + ifname + '" is already compressed.')
            return 1
        ofname = ifname + '.huff'
        if os.path.exists(ofname) :
            print('error: file "' + ofname + '" exists.')
            return 1
        h = huff()
        h.compress(ifname, ofname)
    return 0


if __name__ == '__main__' :
    sys.exit(main())

    
    


