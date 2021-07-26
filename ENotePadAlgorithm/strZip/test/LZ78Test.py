from ENotePadAlgorithm.strZip.LZ78 import *

if __name__ == '__main__':
    # How to use:
    compressed = compress('TOBEORNOTBTOBEORTOEORNOT')
    print (compressed)
    decompressed = decompress(compressed)
    print (decompressed)