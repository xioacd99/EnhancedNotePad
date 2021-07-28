def isBraceValid(str) -> bool:
    symbols = ['(', ')', '[', ']', '{', '}']

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    stk = list()
    for ch in str:
        if ch in symbols:
            if ch in pairs:
                if not stk or stk[-1] != pairs[ch]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(ch)
    return not stk

if __name__ == '__main__':
    ans = isBraceValid('(hello, world)')
    print(ans)
