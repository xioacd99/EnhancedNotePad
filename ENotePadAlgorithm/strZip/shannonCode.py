import math


class ShannonCode(object):
    def __init__(self):
        self.Sump = [0]  # 累加概率
        self.codeLen = []  # 码长
        self.shonCode = []  # 码

    def initList(self, str):  # 初始化列表
        for i in range(0, len(str), 2):
            self.code.append(str[i])
            self.code.append('')

    def FindListIndex(self, str, x):  # 寻找列表某字符序号
        for i, item in enumerate(str):
            if item == x:
                return i

    def sortList(self, str):
        for i in range(1, len(str), 2):
            for j in range(1, len(str) - i, 2):
                if str[j] < str[j + 2]:
                    str[j - 1], str[j + 1] = str[j + 1], str[j - 1]
                    str[j], str[j + 2] = str[j + 2], str[j]
        return str

    def avgCodeLen(self, code, codeLen):
        sumLen = 0.0
        for i in range(1, len(code), 2):
            mid = int((i - 1) / 2)
            sumLen = sumLen + code[i] * codeLen[mid]
        return sumLen

    def countH(self, handleStr):  # 计算信源熵
        sumStrNum = 0
        #   将统计的数量转化为概率
        for i in range(1, len(handleStr), 2):
            sumStrNum = sumStrNum + handleStr[i]
        for i in range(1, len(handleStr), 2):
            handleStr[i] = handleStr[i] / sumStrNum
        sum = 0.0
        sum_1 = 0.0
        for i in range(1, len(handleStr), 2):
            sum_1 += handleStr[i]
            sum += -handleStr[i] * math.log(handleStr[i], 2)
            self.Sump.append(sum_1)
        # print('信源熵为:%.2f' % sum, '(比特/符号)')
        return handleStr

    def FanoCodeLen(self):  # 码长
        for i in range(1, len(self.code), 2):
            self.codeLen.append(len(self.code[i]))

    def codeStrBin(self, temp, codelen):  # 香农编码时使用 小数转二进制并输出对应编码
        sump = self.Sump[temp]
        strCode = ''
        while True:
            sump *= 2
            if sump >= 1:
                strCode = strCode + '1'
            else:
                strCode = strCode + '0'
            sump -= int(sump)
            if sump == 0:
                if len(strCode) != codelen:  # 根据码长来进行补位
                    strCode = strCode + '0' * (codelen - len(strCode))
                    break
        return strCode[:codelen]  # 根据码长将等到的二进制进行截取

    def countCodeLen(self, handleStr):  # 计算码长
        for i in range(1, len(handleStr), 2):
            num_1 = -math.log(handleStr[i], 2)
            num_2 = num_1 + 1
            for i in range(len(handleStr)):
                if num_1 <= i < num_2:
                    self.codeLen.append(i)
                    break

    def Shannon(self, handleStr):
        self.countCodeLen(handleStr)
        for i in range(len(self.codeLen)):
            self.shonCode.insert(i, self.codeStrBin(i, self.codeLen[i]))

    def statistics(self, str):  # 统计字符
        handleStr = []
        for i in str:
            if i != ' ' and i != '"' and i != "." and i != ',':  # 将不需要统计的内容写到此处
                if i in handleStr:
                    num = self.FindListIndex(handleStr, i)
                    handleStr[num + 1] += 1
                else:
                    handleStr.append(i)
                    handleStr.append(1)

        handleStr = self.sortList(handleStr)  # 排序
        handleStr = self.countH(handleStr)  # 计算信源熵
        return handleStr

    def encode(self, msg):
        handleStr = self.statistics(msg)
        self.Shannon(handleStr)

        # 算法测试输出语句
        '''
        for i in range(0, len(handleStr), 2):
            j = int(i / 2)
            print('原始字符:|', handleStr[i], '|概率:', handleStr[i + 1], '|香农码长', codeLen[j], '|香农编码', shonCode[j])
        print('香农平均码长:', averageCodeLen(handleStr, codeLen))
        '''
        # end

        result = ''
        for ch in msg:
            for j in range(0, len(handleStr), 2):
                if ch == handleStr[j]:
                    result += str(self.shonCode[int(j / 2)])
        return result


if __name__ == '__main__':
    test = ShannonCode()
    result = test.encode('hello, world')
    print(result)
