import os

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']

class BruteForce(object):
    def __init__(self):
        pass

    def strBruteForceFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        '''
        @description: 朴素字符串查找
        @param {*} source: 源字符串, target: 目标字符串, pos: 查询开始的位置, fullWord: 是否选择全字查询(True-全字匹配, False-非全字匹配), 是否区分大小写(True-是, False-否)
        @return {*} 返回下标列表
        '''
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        sLen = len(source)
        tLen = len(target)
        i = pos
        j = 0
        idx = []

        while i < sLen:
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

            if j == tLen:
                wordStart = i - j
                # 是否全字匹配
                if fullWord:
                    wordEnd = i
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

    def fileBurteForceFind(self, filename, target):
        '''
        @description: 朴素字符串查找
        @param {*} filename: 文件名
        @param {*} target: 目标字符串
        @return {*} results: 查询结果字符串
        '''
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strBruteForceFind(line, target)
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