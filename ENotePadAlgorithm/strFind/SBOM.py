import os

# import time only for performance test
import time

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']

# SBOM是多对多字符串匹配

class SBOMTreeNode(object):
    def __init__(self):
        super(SBOMTreeNode, self).__init__()
        self.children = {}
        self.bastards = {}
        self.parent = None
        self.isEndPoint = False
        self.endContent = None
        self.suffixTree = None
        self.isTheta = False

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


class SBOMSuffixTree(object):
    def __init__(self):
        super(SBOMSuffixTree, self).__init__()
        self.root = SBOMTreeNode()
        self.length = 0

    def train(self, suffix, endContent):
        currentNode = self.root
        for char in suffix:
            child = currentNode.search(char)
            if child == None:
                newChild = SBOMTreeNode()
                currentNode.adopt(char, newChild)
                newChild.parent = currentNode
                currentNode = newChild
            else:
                currentNode = child
        currentNode.isEndPoint = True
        currentNode.endContent = endContent

        if len(suffix) > self.length:
            self.length = len(suffix)

    def react(self, currentNode, key):
        if currentNode.children != None and key in currentNode.children:
            return currentNode.children[key]
        return None


class SBOMPrefixTree(object):
    def __init__(self):
        super(SBOMPrefixTree, self).__init__()
        self.sNodeTable = {}
        self.root = SBOMTreeNode()
        self.thetaNode = SBOMTreeNode()
        self.thetaNode.isTheta = True
        self.sNodeTable[self.root] = self.thetaNode

    def getSNode(self, currentNode):
        if currentNode in self.sNodeTable:
            return self.sNodeTable[currentNode]
        else:
            return self.thetaNode

    def setSNode(self, currentNode, sNode):
        self.sNodeTable[currentNode] = sNode

    def train(self, sample, endInfo):
        if sample == None or isinstance(sample, str) == False or len(sample) == 0:
            return
        currentNode = self.root
        for i in range(len(sample) - 1, -1, -1):
            char = sample[i]
            child = currentNode.search(char)
            if child == None:
                newChild = SBOMTreeNode()
                currentNode.adopt(char, newChild)
                newChild.parent = currentNode
                currentNode = newChild
            else:
                currentNode = child
        currentNode.isEndPoint = True
        currentNode.suffixTree = SBOMSuffixTree()
        for endItem in endInfo:
            currentNode.suffixTree.train(endItem['suffix'], endItem['content'])

    def automatizeSeeker(self, currentNode, kNode, jumpKey):
        if kNode.isTheta == True:
            self.setSNode(currentNode, self.root)
        else:
            if jumpKey in kNode.children or jumpKey in kNode.bastards:
                jNode = None
                if jumpKey in kNode.children:
                    jNode = kNode.children[jumpKey]
                else:
                    jNode = kNode.bastards[jumpKey]
                self.setSNode(currentNode, jNode)
            else:
                kNode.bastards[jumpKey] = currentNode
                self.automatizeSeeker(currentNode, self.getSNode(kNode), jumpKey)

    def automatizeLoop(self, currentLayerNodes):
        if currentLayerNodes == None or len(currentLayerNodes) == 0:
            return
        nextLayerNodes = []
        for currentLayerNodeItem in currentLayerNodes:
            currentLayerNode = currentLayerNodeItem['node']
            self.automatizeSeeker(currentLayerNode, self.getSNode(currentLayerNode.parent),
                                    currentLayerNodeItem['key'])
            if currentLayerNode.children != None and len(currentLayerNode.children) > 0:
                for childKey, childNode in currentLayerNode.children.items():
                    nextLayerNodeItem = {'key': childKey, 'node': childNode}
                    nextLayerNodes.append(nextLayerNodeItem)
        self.automatizeLoop(nextLayerNodes)

    def automatize(self):
        nextLayerNodes = []
        for childKey, childNode in self.root.children.items():
            nodeItemTmp = {'key': childKey, 'node': childNode}
            nextLayerNodes.append(nodeItemTmp)
        self.automatizeLoop(nextLayerNodes)

    def react(self, currentNode, key):
        if currentNode.children != None and key in currentNode.children:
            return currentNode.children[key]
        if currentNode.bastards != None and key in currentNode.bastards:
            return currentNode.bastards[key]
        return None


class SBOMUtil(object):
    def __init__(self):
        super(SBOMUtil, self).__init__()
        self.samples = []
        self.searchWindowLen = 0
        self.samplePrefixDic = {}
        self.prefixTree = SBOMPrefixTree()

    def train(self, sample):
        if sample == None or isinstance(sample, str) == False or len(sample) == 0:
            return
        self.samples.append(sample)
        sampleLen = len(sample)
        if len(self.samples) == 1:
            self.searchWindowLen = sampleLen
        elif sampleLen < self.searchWindowLen:
            self.searchWindowLen = sampleLen

    def prepare(self):
        # cut samples
        self.samplePrefixDic = {}
        for sampleItem in self.samples:
            prefix = sampleItem[0: self.searchWindowLen]
            suffix = sampleItem[self.searchWindowLen: len(sampleItem)]
            dicItemTmp = {'content': sampleItem, 'suffix': suffix}
            prefixDics = []
            if prefix in self.samplePrefixDic:
                prefixDics = self.samplePrefixDic[prefix]
            prefixDics.append(dicItemTmp)
            self.samplePrefixDic[prefix] = prefixDics

        # build prefix tree
        self.prefixTree = SBOMPrefixTree()
        for prefix, prefixDics in self.samplePrefixDic.items():
            self.prefixTree.train(prefix, prefixDics)

        # automatize
        self.prefixTree.automatize()

    def saveSearchResult(self, resultDic, sample, location):
        listTmp = []
        if sample in resultDic:
            listTmp = resultDic[sample]
        listTmp.append(location)
        resultDic[sample] = listTmp
        return resultDic

    def search(self, content):
        result = {}
        if content == None or isinstance(content, str) == False or len(content) < self.searchWindowLen:
            return result

        contentLen = len(content)
        offset = 0
        while True:
            if self.searchWindowLen + offset > contentLen:
                break
            currentNode = self.prefixTree.root
            finded = True
            stopIndex = offset + 1
            for i in range(offset + self.searchWindowLen - 1, offset - 1, -1):
                contentChar = content[i]
                nextNodeTmp = self.prefixTree.react(currentNode, contentChar)
                if nextNodeTmp == None:
                    stopIndex = i + 1
                    finded = False
                    break
                else:
                    currentNode = nextNodeTmp
            if finded == True:
                if currentNode.isEndPoint and currentNode.suffixTree != None:
                    currentSuffixNode = currentNode.suffixTree.root
                    j = 1
                    while True:
                        if currentSuffixNode.isEndPoint == True:
                            self.saveSearchResult(result, currentSuffixNode.endContent, offset)
                        indexTmp = self.searchWindowLen + offset + j - 1
                        if indexTmp >= contentLen:
                            break
                        currentSuffixNodeTmp = currentNode.suffixTree.react(currentSuffixNode, content[indexTmp])
                        if currentSuffixNodeTmp == None:
                            break
                        else:
                            currentSuffixNode = currentSuffixNodeTmp
                        j = j + 1
                offset = offset + 1
            else:
                offset = stopIndex
        return result


class SBOM(object):
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
        trainsString=''
        sbomUtil = SBOMUtil()
        samples = source.split(' ')
        for sample in samples:
            trainsString = trainsString+', '+sample
            sbomUtil.train(sample)
        sbomUtil.prepare()

        for value in target:
            idx.append(sbomUtil.search(value)[target])

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
    test = SBOM()
    ans = test.fileFind(
        'F:\\.vscode\\Github\\EnhancedNotePad\\ENotePadAlgorithm\\algorithmTestData\\BigTest.txt', 'be')
    # end

    end = time.time()
    print('using time: %s seconds' % (end - start))