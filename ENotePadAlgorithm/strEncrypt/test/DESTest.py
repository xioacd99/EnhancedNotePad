from ENotePadAlgorithm.strEncrypt.DES import *

#main
#key  123456789abcdef0
#text 0123456789abcdef
if __name__ == "__main__": # __main__
    flag = ''
    print("if you want to encode input 0 or input 1 to decode\n")
    flag = int(input())
    if flag == 0:
        print("格式：0123456789abcdef\n请输入明文：\n")
        text = input()
        print("请输入密钥\n")
        key = input()
        cipher = encode(text,key)
        print("密文为："+cipher)
    else:
        print("格式：0123456789abcdef\n请输入密文：\n")
        cipher = input()
        print("请输入密钥\n")
        key = input()
        text = encode(cipher,key,2)
        print("明文为："+text)
