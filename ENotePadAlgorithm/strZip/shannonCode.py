import math

Sump = [0]  # 累加概率
codeLen = []  # 香农码长
fcodeLen = []  # 费诺码长
shonCode = []  # 香农码
FanoCode = []  # 费诺码


def initList(handleStr):  # 初始化列表
    for i in range(0, len(handleStr), 2):
        FanoCode.append(handleStr[i])
        FanoCode.append('')


def FindListIndex(str_list, x):  # 寻找列表某字符序号
    for i, item in enumerate(str_list):
        if item == x:
            return i


def sortList(List_1):  # 排序 得到一个排序好的概率分布
    for i in range(1, len(List_1), 2):
        for j in range(1, len(List_1) - i, 2):
            if List_1[j] < List_1[j + 2]:
                List_1[j - 1], List_1[j + 1] = List_1[j + 1], List_1[j - 1]
                List_1[j], List_1[j + 2] = List_1[j + 2], List_1[j]
    return List_1


def averageCodeLen(codeList, codelenlist):  # 计算平均码长
    sumLen = 0.0
    for i in range(1, len(codeList), 2):
        mid = int((i - 1) / 2)
        sumLen = sumLen + codeList[i] * codelenlist[mid]
    return sumLen


def Statistics(sourceStr):  # 统计字符
    handleStr = []
    for i in sourceStr:
        if i != ' ' and i != '"' and i != "." and i != ',':  # 将不需要统计的内容写到此处
            if i in handleStr:
                num = FindListIndex(handleStr, i)
                handleStr[num + 1] += 1
            else:
                handleStr.append(i)
                handleStr.append(1)

    handleStr = sortList(handleStr)  # 排序
    handleStr = countH(handleStr)  # 计算信源熵
    return handleStr


def codeStrBin(temp, codelen):  # 香农编码时使用 小数转二进制并输出对应编码
    sump = Sump[temp]
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


def countCodeLen(handleStr):  # 计算码长
    for i in range(1, len(handleStr), 2):
        num_1 = -math.log(handleStr[i], 2)
        num_2 = num_1 + 1
        for i in range(len(handleStr)):
            if num_1 <= i < num_2:
                codeLen.append(i)
                break


def countH(handleStr):  # 计算信源熵
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
        Sump.append(sum_1)
    print('信源熵为:%.2f' % sum, '(比特/符号)')
    return handleStr


def FanoCodeLen():  # 费诺码长
    for i in range(1, len(FanoCode), 2):
        fcodeLen.append(len(FanoCode[i]))


def Shannon(handleStr):  # 香农
    countCodeLen(handleStr)
    for i in range(len(codeLen)):
        shonCode.insert(i, codeStrBin(i, codeLen[i]))


def Fano(handleStr):	# 费诺
    if len(handleStr) == 2:  # 当分组只有一个时不应再继续分组和编码,退出
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
    #   编码 在中间位置之前的字符为0，之后的为1
    str0, str1 = "0", "1"
    for i in range(0, len(handleStr), 2):
        if i < findPosition:
            temp = FindListIndex(FanoCode, handleStr[i])
            FanoCode[temp + 1] = FanoCode[temp + 1] + str0
        else:
            temp = FindListIndex(FanoCode, handleStr[i])
            FanoCode[temp + 1] = FanoCode[temp + 1] + str1

    # 分组 分成左右两部分来进行递归
    leftGroup = []
    rightGroup = []
    # 对左右两部分进行填充
    for j in range(findPosition + 1):
        leftGroup.append(handleStr[j])
    for j in range(findPosition + 1, len(handleStr)):
        rightGroup.append(handleStr[j])

    # 递归分组编码
    Fano(leftGroup)
    Fano(rightGroup)

if __name__ == '__main__':
    sourceStr = input("请输入想要编码字符:")
    handleStr = Statistics(sourceStr)
    Shannon(handleStr)
    initList(handleStr)
    Fano(handleStr)
    FanoCodeLen()
    for i in range(0, len(handleStr), 2):
        j = int(i / 2)
        print('原始字符:|', handleStr[i], '|概率:', handleStr[i + 1], '|香农码长', codeLen[j], '|香农编码', shonCode[j], '|费诺码长',
              fcodeLen[j], '|费诺编码', FanoCode[i + 1])
    print('香农平均码长:', averageCodeLen(handleStr, codeLen))
    print('费诺平均码长:', averageCodeLen(handleStr, fcodeLen))