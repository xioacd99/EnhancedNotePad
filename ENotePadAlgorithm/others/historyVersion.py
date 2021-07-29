import os

from ENotePadAlgorithm.strFind.KMP import *


# 物理存储(栈)
# 因为是追加写，所以最新的会在最后，所以读下一行就可以了

def getVersionCode(dataFilename, filename):
    # 这里用KMP做测试用，实际使用特定环境配置下性能最高的或安全性最高的
    Find = KMP()
    if os.path.exists(dataFilename):
        with open(dataFilename, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                if Find.strFind(line, filename):
                    return line[len(filename):]
                line = file.readline()
    else:
        with open(dataFilename, 'w', encoding='utf-8') as file:
            print('Create a new history version data file')
    return str(-1)


def getFilePath(filename):
    # 这里用KMP做测试用，实际使用特定环境配置下性能最高的或安全性最高的
    Find = KMP()
    # 测试版本号1-100的文件是否存在，默认只存储100个历史版本
    for versionCode in range(1, 101):
        if os.path.exists(filename + str(versionCode)):
            return os.getcwd()
        else:
            return str(-1)


class HistoryVersion(object):
    # 读取已有信息，初始化栈
    def __init__(self):
        self.data = []
        self.Find = KMP()

    def saveFile(self, dataFilename, filename):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'a+', encoding='utf-8') as dfile:
                line = dfile.readline()
                while line:
                    if self.Find.strFind(line, filename):
                        dfile.write('%s version: %s' % filename, str(getVersionCode(dataFilename, filename) + str(1)))
                        with open(filename, 'r', encoding='utf-8') as file:
                            content = file.readlines()
                            dfile.write(content)
                    line = dfile.readline()
        else:
            with open(dataFilename, 'w', encoding='utf-8') as dfile:
                print('Create a new history version data file')

    def getPrevioisVersion(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'r', encoding='utf-8') as dfile:
                line = dfile.readline()
                tmp = line
                while line:
                    line = dfile.readline()
                    if self.Find.strFind(line, filename) and getVersionCode(dataFilename, filename) == versionCode:
                        return getFilePath(tmp)
                    tmp = line
        else:
            with open(dataFilename, 'w', encoding='utf-8') as dfile:
                print('Create a new history version data file')

    def getNextVersion(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'r', encoding='utf-8') as dfile:
                line = dfile.readline()
                while line:
                    if self.Find.strFind(line, filename) and getVersionCode(dataFilename, filename) == versionCode:
                        line = dfile.readline()
                        return getFilePath(line)
                    line = dfile.readline()
        else:
            with open(dataFilename, 'w', encoding='utf-8') as dfile:
                print('Create a new history version data file')

    def clearHistory(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'w', encoding='utf-8') as dfile:
                dfile.truncate()
        else:
            with open(dataFilename, 'w', encoding='utf-8') as dfile:
                print('Create a new history version data file')
