import os

# import time only for performance test
import time

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class ShiftAnd(object):
    def preprocess(self, t):
        B = {}
        for i in range(len(t)):
            c = t[i]
            if c in B:
                B[c] |= (1 << i)
            else:
                B[c] = 1 << i
        return B

    def strFind(self, source, target, pos=0, fullWord=True, caseSensitive=True):
        sLen = len(source)
        tLen = len(target)

        # 如果主串和子串有一方为空或子串长度小于主串则返回空
        if (sLen == 0 or tLen == 0) or tLen < sLen:
            return []

        # 如果不区分大小写
        if not caseSensitive:
            source = source.lower()
            target = target.lower()

        idx = []

        B = self.preprocess(target)
        D = 0
        mask = 1 << (tLen - 1)
        for i in range(sLen):
            ch = source[i]
            if ch in B:
                D = ((D << 1) | 1) & B[ch]
            else:
                D = 0
            if (D & mask):
                wordStart = i - tLen + 1
                # 是否全字匹配
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
            with open(filename, 'r', encoding='utf-8') as file:
                line = file.readline()
                while line:
                    idx = self.strFind(line, target)
                    if idx:
                        for pos in idx:
                            results.append([lineNum, pos])

                        # 算法测试输入语句
                        '''
                        singleResult = 'The ' + target + ' occurs ' + str(len(idx)) + ' times in line ' + str(
                            lineNum) + ', which positions are '
                        for pos in idx:
                            singleResult += '(' + str(lineNum) + ', ' + str(pos) + ') '
                        results.append(singleResult)
                        '''

                    line = file.readline()
                    lineNum += 1
        else:
            with open(filename, 'w', encoding='uft-8') as file:
                print('Create a new file named %s' % filename)
        return results


if __name__ == '__main__':
    start = time.time()

    # write your test code
    test = ShiftAnd()
    ans = test.fileFind(
        'F:\\.vscode\\Github\\EnhancedNotePad\\ENotePadAlgorithm\\algorithmTestData\\BigTest.txt', 'be')
    # end

    end = time.time()
    print('using time: %s seconds' % (end - start))
