class LZ77(object):
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.buffer_size = 4

    def longest_match(self, data, cursor):
        end_buffer = min(cursor + self.buffer_size, len(data))

        p = -1
        l = -1
        c = ''

        for j in range(cursor+1, end_buffer+1):
            start_index = max(0, cursor - self.window_size + 1)
            substring = data[cursor + 1:j + 1]

            for i in range(start_index, cursor+1):
                repetition = len(substring) / (cursor - i + 1)
                last = len(substring) % (cursor - i + 1)
                matchedstring = data[i:cursor + 1] * int(repetition) + data[i:i + last]

                if matchedstring == substring and len(substring) > l:
                    p = cursor - i + 1
                    l = len(substring)
                    c = data[j+1]

        if p == -1 and l == -1:
            return 0, 0, data[cursor + 1]
        return p, l, c

    def encode(self, str):
        i = -1
        out = []

        while i < len(str)-1:
            (p, l, c) = self.longest_match(str, i)
            out.append((p, l, c))
            i += (l+1)
        return out

if __name__ == '__main__':
    test=LZ77()
    result = test.encode('aacaacabcabaaac')
    print (result)
