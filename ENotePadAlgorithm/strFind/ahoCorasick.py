import os

# import time only for performance test
import time

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class ACTireTreeNode(object):
    def __init__(self):
        self.children = {}
        self.parent = None
        self.bastard = None
        self.isEndPoint = False
        self.endContent = None

    def search(self, content):
        if content == None or isinstance(content, str) == False or len(content) == 0:
            return None
        result = None
        for key, value in self.children.items():
            if key == content:
                result = value
                break
        return result

    def adopt(self, key, node):
        if key == None or len(key) == 0 or node == None:
            return
        self.children[key] = node


class ACTireTree(object):

    def __init__(self):
        self.root = ACTireTreeNode()
        self.__keyForTerminal = 'terminal'
        self.__keyForPassing = 'passing'

    def train(self, sample):
        if sample == None or isinstance(sample, str) == False or len(sample) == 0:
            return
        currentNode = self.root
        for char in sample:
            child = currentNode.search(char)
            if child == None:
                newChild = ACTireTreeNode()
                currentNode.adopt(char, newChild)
                newChild.parent = currentNode
                currentNode = newChild
            else:
                currentNode = child

        currentNode.isEndPoint = True
        currentNode.endContent = sample

    def __automatizeLoop(self, currentKey, currentNode):
        if currentNode.bastard == None:
            if currentNode.parent == None:
                currentNode.bastard = self.root
            elif currentNode.parent == self.root:
                currentNode.bastard = self.root
            else:
                tmpBastard = self.root
                tmpParent = currentNode.parent
                while True:
                    if tmpParent.bastard == None:
                        break
                    elif tmpParent.bastard.children == None or len(tmpParent.bastard.children) == 0:
                        tmpParent = tmpParent.parent
                    else:
                        finded = False
                        for key, child in tmpParent.bastard.children.items():
                            if key == currentKey:
                                finded = True
                                tmpBastard = child
                                break
                        if finded == False:
                            tmpParent = tmpParent.parent
                        break
                currentNode.bastard = tmpBastard
        if len(currentNode.children) > 0:
            for key, child in currentNode.children.items():
                self.__automatizeLoop(key, child)

    def automatize(self):
        self.__automatizeLoop(None, self.root)

    def __buildBlankResult(self):
        return {self.__keyForTerminal: self.root, self.__keyForPassing: []}

    def __react(self, currentNode, key):
        result = self.__buildBlankResult()
        if currentNode == None:
            return result
        currentNodeTmp = currentNode
        resultTerminal = self.root
        resultPassing = []
        while True:
            if currentNodeTmp.children == None or len(currentNodeTmp.children) == 0:
                # jump
                currentNodeTmp = currentNodeTmp.bastard
                resultPassing.append(currentNodeTmp)
                continue

            rightChild = None
            for keyTmp, child in currentNodeTmp.children.items():
                if keyTmp == key:
                    rightChild = child
                    break
            if rightChild == None:
                if currentNodeTmp == self.root:
                    # stop
                    resultTerminal = currentNodeTmp
                    break
                else:
                    # jump
                    currentNodeTmp = currentNodeTmp.bastard
                    resultPassing.append(currentNodeTmp)
            else:
                # stop
                resultTerminal = rightChild
                break
        result[self.__keyForTerminal] = resultTerminal
        result[self.__keyForPassing] = resultPassing
        return result

    def react(self, currentNode, key):
        if key == None or isinstance(key, str) == False or len(key) == 0:
            return self.__buildBlankResult()
        return self.__react(currentNode, key)


class AhoCorasickUtil(object):
    def __init__(self):
        super(AhoCorasickUtil, self).__init__()
        self.__acTree = ACTireTree()

    def train(self, sample):
        self.__acTree.train(sample)

    def prepare(self):
        self.__acTree.automatize()

    def __saveSearchResult(self, resultDic, node, location):
        if resultDic == None:
            resultDic = {}
        if node == None:
            return resultDic
        key = node.endContent
        value = location - len(node.endContent) + 1
        listTmp = []
        if key in resultDic:
            listTmp = resultDic[key]
        listTmp.append(value)
        resultDic[key] = listTmp
        return resultDic

    def search(self, content):
        result = {}
        nodeTmp = self.__acTree.root
        contentLength = len(content)
        for i in range(0, contentLength, 1):
            resultTmp = self.__acTree.react(nodeTmp, content[i])
            nextNode = resultTmp['terminal']
            nodeNeedSave = nextNode
            while True:
                if nodeNeedSave == None:
                    break
                if nodeNeedSave.isEndPoint == True:
                    result = self.__saveSearchResult(result, nodeNeedSave, i)
                nodeNeedSaveTmp = nodeNeedSave.bastard
                if nodeNeedSave == self.__acTree.root and nodeNeedSave == nodeNeedSaveTmp:
                    break
                nodeNeedSave = nodeNeedSaveTmp
            nodeTmp = nextNode
        return result


class AhoCorasick(object):
    # 限制精确匹配 (从0开始, 全字匹配)
    def strFind(self, source, target, caseSensitive=True):
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
        trainString = ''
        acUtil = AhoCorasickUtil()
        samples = source.split(' ')
        for sample in samples:
            trainString = trainString + ', ' + sample
            acUtil.train(sample)
        acUtil.prepare()

        for value in target:
            idx.append(acUtil.search(value)[target])

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
    test = AhoCorasick()
    ans = test.fileFind(
        'F:\\.vscode\\Github\\EnhancedNotePad\\ENotePadAlgorithm\\algorithmTestData\\BigTest.txt', 'be')
    # end

    end = time.time()
    print('using time: %s seconds' % (end - start))
