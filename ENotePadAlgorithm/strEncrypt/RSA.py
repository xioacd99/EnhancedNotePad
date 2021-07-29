#!/usr/bin/env python3
# -*- coding: utf-8 -*-

llen = 512
import random

def qp(a, x, mod=1e9 + 7):
    ans = 1;
    a %= mod
    while x:
        if x & 1:
            ans = a * ans % mod
        a = a * a % mod
        x >>= 1
    return ans


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def egcd(a, b, x, y):  # return ans,x,y
    if b == 0: return 1, 0
    x, y = egcd(b, a % b, x, y)
    temp = x
    x = y
    y = temp - a // b * y  # // stand 整除
    return x, y


def inverse(a, mod):
    x, y = 1, 1
    x, y = egcd(a, mod, x, y)
    return (x % mod + mod) % mod


def mltest(n, times=50):
    if (n == 2): return True
    if (n < 2 or not (n & 1)): return False
    temp = 0
    u = n - 1
    while (u & 1) == 0:
        temp += 1
        u >>= 1
    for i in range(times):
        a = random.randint(1, n - 1)
        x = qp(a, u, n)
        for j in range(temp):
            y = x * x % n
            if y == 1 and x != 1 and x != n - 1: return False
            x = y
        if x != 1: return False
    return True


def gprime():
    p = 0
    while not p:
        temp = random.randint(1, (1 << llen) - 1)
        if mltest(temp): p = temp
    return p


def strEncrypt(text):
    p, q = gprime(), gprime()
    while (p == q): q = gprime()
    n = p * q;
    fn = (p - 1) * (q - 1)
    e = 0
    while 1:
        e = random.randint(2, fn - 1)
        if gcd(e, fn) == 1: break

    pkey = inverse(e, fn)
    cipher = qp(text, e, n)
    return e, n, cipher, pkey, p, q


if __name__ == "__main__":
    text = 12345
    e, n, cipher, pk, p, q = strEncrypt(text)
    print("public key b: \n", e, "\nn:", n, "\ncipher:", cipher, "\nprivite key:", pk, "\np:", p, "\nq:", q)
