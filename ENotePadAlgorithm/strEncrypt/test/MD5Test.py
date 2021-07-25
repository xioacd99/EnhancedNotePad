from ENotePadAlgorithm.strEncrypt.MD5 import MD5

if __name__ == '__main__':
    message = input("输入要加密的字符串：")
    MD5 = MD5(message)
    MD5.fill_text()
    result = MD5.group_processing()
    print("32位小写MD5加密：{}".format(result))