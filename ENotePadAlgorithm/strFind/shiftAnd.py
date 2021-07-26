import os

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class ShiftAnd(object):
    def __init__(self):
        pass

    def preprocess(self, t):
        B = {}
        for i in range(len(t)):
            c = t[i]
            if c in B:
                B[c] |= (1 << i)
            else:
                B[c] = 1 << i
        return B

    def strFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        idx = []
        sLen = len(source)
        tLen = len(target)

        B = self.preprocess(target)
        D = 0
        mask = 1 << (tLen - 1)
        for i in range(sLen):
            ch = source[i]
            if ch in B:
                D = ((D << 1) | 1) & B[ch]
            else:
                D = 0
            if (D&mask):
                wordStart = i - tLen + 1
                if fullWord:
                    wordEnd = wordStart
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - wordStart == tLen:
                        idx.append(wordStart)
                else:
                    idx.append(wordStart)
        return idx

    def fileFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strFind(line, target)
                    if idx:
                        # 生成查询字符串前半部分
                        singleResult = 'The ' + target + ' occurs ' + str(len(idx)) + ' times in line ' + str(
                            lineNum) + ', which positions are '
                        # 添加每行的具体位置
                        for pos in idx:
                            singleResult += '(' + str(lineNum) + ', ' + str(pos) + ') '
                        results.append(singleResult)
                    line = file.readline()
                    lineNum += 1
        else:
            with open(filename, 'w') as file:
                print('Create a new file named %s' % filename)
        return results


if __name__ == '__main__':
    s = 'be being be being '
    t = 'be'
    res = shift_and_match(s, t)
    print('Find "%s" in "%s" by positions: ' % (t, s), res)
