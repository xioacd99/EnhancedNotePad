import os

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']

class Sunday(object):
    def __init__(self):
        pass

    def strSundayFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        sLen = len(source)
        tLen = len(target)
        idx = []

        i = 0
        while i <= sLen - tLen:
            if source[i:i + tLen] == target:
                # 是否全字匹配
                if fullWord:
                    wordEnd = i
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - i == tLen:
                        idx.append(i)
                else:
                    idx.append(i)
                i += tLen
            else:
                rpos = target.rfind(source[i + tLen])
                if rpos == -1:
                    i += (tLen + 1)
                else:
                    i += (tLen - rpos)
        return idx

    def fileSundayFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strSundayFind(line, target)
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