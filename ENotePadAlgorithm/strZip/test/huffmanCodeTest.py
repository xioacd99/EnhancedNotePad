from ENotePadAlgorithm.strZip.huffmanCode import *

if __name__ == '__main__':
    text = input('The text to encode:')
    chars_freqs = count_freq(text)
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)

    huffmanStr = encodeStr(text, chars_freqs, codes)
    print('Encode result:' + huffmanStr)
    orignStr = decodeStr(huffmanStr, chars_freqs, codes)
    print('Decode result:' + orignStr)