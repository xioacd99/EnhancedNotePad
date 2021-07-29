class RLC(object):
    def encode(self, msg):
        strList = []
        cnt = 1
        for i in range(0, len(msg)):
            if i + 1 < len(msg) and msg[i] == msg[i + 1]:
                cnt += 1
            else:
                strList.append(msg[i])
                strList.append(cnt)
                cnt = 1

        buffer = ""
        for index, value in enumerate(strList):
            if index % 2 == 0:
                buffer += "(" + str(value) + ","
            else:
                buffer += str(value) + "),"
        buffer = buffer.rstrip(',')
        result = buffer.replace(',', '').replace('(', '').replace(')', '')
        return result


if __name__ == '__main__':
    test = RLC()
    ans = test.encode('aabbbcccc')
    print(ans)
