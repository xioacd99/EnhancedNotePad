import os


# 因为是追加写，所以最新的会在最后，所以读下一行就可以了

# 这里调用字符串匹配
def strFind(source, target):
    pass


def getVersionCode(dataFilename, filename):
    pass


def getFilePath(record):
    pass


class HistoryVersion(object):
    # 读取已有信息，初始化栈
    def __init__(self):
        self.data = []

    def saveFile(self, dataFilename, filename):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'a+') as dfile:
                line = dfile.readline()
                while line:
                    if strFind(line, filename):
                        dfile.write('%s version: %d' % filename, getVersionCode(dataFilename, filename) + 1)
                        with open(filename, 'r') as file:
                            content = file.readlines()
                            dfile.write(content)
                    line = dfile.readline()
        else:
            with open(dataFilename, 'w') as dfile:
                print('Create a new history version data file')

    def getPrevioisVersion(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'r') as dfile:
                line = dfile.readline()
                tmp = line
                while line:
                    line = dfile.readline()
                    if strFind(line, filename) and getVersionCode(dataFilename, filename) == versionCode:
                        return getFilePath(tmp)
                    tmp = line
        else:
            with open(dataFilename, 'w') as dfile:
                print('Create a new history version data file')

    def getNextVersion(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'r') as dfile:
                line = dfile.readline()
                while line:
                    if strFind(line, filename) and getVersionCode(dataFilename, filename) == versionCode:
                        line = dfile.readline()
                        return getFilePath(line)
                    line = dfile.readline()
        else:
            with open(dataFilename, 'w') as dfile:
                print('Create a new history version data file')

    def clearHistory(self, dataFilename, filename, versionCode):
        if os.path.exists(dataFilename):
            with open(dataFilename, 'w') as dfile:
                dfile.truncate()
        else:
            with open(dataFilename, 'w') as dfile:
                print('Create a new history version data file')
