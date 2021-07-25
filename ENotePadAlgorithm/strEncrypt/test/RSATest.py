from ENotePadAlgorithm.strEncrypt.RSA import *

if __name__ == "__main__": #main
    #text = int(input())
    text = 1
    tencode = time.time()
    e,n,cipher,pk,p,q = encode(text)
    tencode = time.time() - tencode
    print("public key b: \n",e,"\nn:",n,"\ncipher:",cipher,"\nprivite key:",pk,"\np:",p,"\nq:",q)
    tdecode = time.time()
    print("明文为",decode(cipher,pk,n))
    tdecode = time.time() - tdecode
    print("加密时间为：",tencode,"\n解密时间为: ",tdecode)