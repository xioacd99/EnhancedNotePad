import os

# import time only for performance test
import time

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class KMP(object):
    def getNextTable(self, word):
        if len(word) == 0:
            return []

        i = 0
        j = -1
        lenth = len(word)
        next = [0] * lenth
        next[0] = -1

        # 因为比较的是 t[i + 1]
        while i < lenth - 1:
            if j == -1 or word[i] == word[j]:
                i += 1
                j += 1
                if word[i] != word[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]
        return next

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

        next = self.getNextTable(target)
        i = pos
        j = 0
        idx = []

        while i < sLen:
            if j == -1 or source[i] == target[j]:
                i += 1
                j += 1
            else:
                j = next[j]

            if j == tLen:
                wordStart = i - j
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
                j = 0
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
    test = KMP()
    ans = test.fileFind(
        'F:\\.vscode\\Github\\EnhancedNotePad\\ENotePadAlgorithm\\algorithmTestData\\BigTest.txt', 'be')
    # end

    end = time.time()
    print('using time: %s seconds' % (end - start))
