import math


class FanoCode(object):
    def __init__(self):
        self.Sump = [0]  # 累加概率
        self.codeLen = []  # 码长
        self.code = []  # 码

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

    def statistics(self, originStr):  # 统计字符
        result = []
        for i in originStr:
            # 不需要统计的字符
            if i != ' ' and i != '"' and i != "." and i != ',':
                if i in result:
                    num = self.FindListIndex(result, i)
                    result[num + 1] += 1
                else:
                    result.append(i)
                    result.append(1)

        result = self.sortList(result)  # 排序
        result = self.countH(result)  # 计算信源熵
        return result

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

    def Fano(self, handleStr):
        # 当分组只有一个时不应再继续分组和编码, 退出
        if len(handleStr) == 2:
            return

        # 初始化
        findPosition = 1
        sump = 0
        dif = 1
        midNum = 0
        # 计算一下当前概率和的中间值
        for i in range(1, len(handleStr), 2):
            midNum = midNum + handleStr[i]
        midNum = midNum / 2

        #   通过累加概率与中间值相减的绝对值，判断从哪里截段
        for i in range(1, len(handleStr), 2):
            sump = sump + handleStr[i]
            dif1 = abs(sump - midNum)
            if dif1 < dif:
                dif = dif1
                findPosition = i
        # 编码 在中间位置之前的字符为0, 之后的为1
        str0, str1 = "0", "1"
        for i in range(0, len(handleStr), 2):
            if i < findPosition:
                temp = self.FindListIndex(self.code, handleStr[i])
                self.code[temp + 1] = self.code[temp + 1] + str0
            else:
                temp = self.FindListIndex(self.code, handleStr[i])
                self.code[temp + 1] = self.code[temp + 1] + str1

        # 分组 分成左右两部分来进行递归
        leftGroup = []
        rightGroup = []
        # 对左右两部分进行填充
        for j in range(findPosition + 1):
            leftGroup.append(handleStr[j])
        for j in range(findPosition + 1, len(handleStr)):
            rightGroup.append(handleStr[j])

        # 递归分组编码
        self.Fano(leftGroup)
        self.Fano(rightGroup)

    def encode(self, msg):
        handleStr = self.statistics(msg)
        self.initList(handleStr)
        self.Fano(handleStr)
        self.FanoCodeLen()

        # 算法测试输出语句
        '''
        for i in range(0, len(handleStr), 2):
            j = int(i / 2)
            print('原始字符:|', handleStr[i], '|概率:', handleStr[i + 1], '|费诺码长',
                  self.codeLen[j], '|费诺编码', self.code[i + 1])
        print('费诺平均码长:', self.avgCodeLen(handleStr, self.codeLen))
        '''
        # end

        result = ''
        for ch in msg:
            for j in range(0, len(handleStr), 2):
                if ch == handleStr[j]:
                    result += str(self.code[j + 1])
        return result


if __name__ == '__main__':
    test = FanoCode()
    result = test.encode('hello, world')
    print(result)
