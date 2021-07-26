from ENotePadAlgorithm.strZip.LZ77 import *

if __name__ == '__main__':
    compressor = LZ77(6)
    origin = list('aacaacabcabaaac')
    pack = compressor.compress(origin)
    unpack = compressor.decompress(pack)
    print (pack)
    print (unpack)
    print (unpack == 'aacaacabcabaaac')