class LZ78(object):
    def encode(self, str):
        dict_size = 256
        dictionary = dict((chr(i), chr(i)) for i in range(dict_size))

        w = ""
        result = []
        for c in str:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c
        if w:
            result.append(dictionary[w])
        return result


if __name__ == '__main__':
    test = LZ78()
    ans = test.encode('tobeornottobetobeornottobetobeornot')
    print(ans)
