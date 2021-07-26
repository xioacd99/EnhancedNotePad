from ENotePadAlgorithm.strZip.shannonCode import *

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