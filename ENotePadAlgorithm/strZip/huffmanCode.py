def count_freq(str):
    chars = []
    chars_freqs = []
    for i in range(0, len(str)):
        if str[i] in chars:
            pass
        else:
            chars.append(str[i])
            char_freq = (str[i], str.count(str[i]))
            chars_freqs.append(char_freq)
    return chars_freqs


class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


class HuffmanCode(object):
    def createNodes(self, freqs):
        return [Node(freq) for freq in freqs]

    def createHuffmanTree(self, nodes):
        queue = nodes[:]
        while len(queue) > 1:
            queue.sort(key=lambda item: item.freq)
            node_left = queue.pop(0)
            node_right = queue.pop(0)
            node_father = Node(node_left.freq + node_right.freq)
            node_father.left = node_left
            node_father.right = node_right
            node_left.father = node_father
            node_right.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]

    def huffmanEncoding(self, nodes, root):
        codes = [''] * len(nodes)
        for i in range(len(nodes)):
            node_tmp = nodes[i]
            while node_tmp != root:
                if node_tmp.isLeft():
                    codes[i] = '0' + codes[i]
                else:
                    codes[i] = '1' + codes[i]
                node_tmp = node_tmp.father
        return codes

    def encodeStr(self, str, chars_freqs, codes):
        huffmanStr = ''
        for char in str:
            i = 0
            for item in chars_freqs:
                if char == item[0]:
                    huffmanStr += codes[i]
                i += 1
        return huffmanStr

    def encode(self, str):
        chars_freqs = count_freq(str)
        nodes = self.createNodes([item[1]] for item in chars_freqs)
        root = self.createHuffmanTree(nodes)
        codes = self.huffmanEncoding(nodes, root)
        return self.encodeStr(str, chars_freqs, codes)


if __name__ == '__main__':
    test = HuffmanCode()
    result = test.encode('hello, world')
    print(result)
