class BWT(object):
    def encode(self, str):
        str += '$'
        table = [str[index:] + str[:index] for index, _ in enumerate(str)]
        table.sort()
        result = [rotation[-1] for rotation in table]
        result = ''.join(result)

        return result.replace('$', '')


if __name__ == '__main__':
    test = BWT()
    result = test.encode('hello, world')
    print(result)
