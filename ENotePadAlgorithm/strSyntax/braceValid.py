class SyntaxBrace(object):
    def __init__(self):
        self.symbols = ['(', ')', '[', ']', '{', '}']
        self.pairs = {')': '(', ']': '[', '}': '{', }

    def isValid(self, str) -> bool:
        stk = list()
        for ch in str:
            if ch in self.symbols:
                if ch in self.pairs:
                    if not stk or stk[-1] != self.pairs[ch]:
                        return False
                    else:
                        stk.pop()
                else:
                    stk.append(ch)
        return not stk


if __name__ == '__main__':
    test = SyntaxBrace()
    print(test.isValid('(hello, world)'))
