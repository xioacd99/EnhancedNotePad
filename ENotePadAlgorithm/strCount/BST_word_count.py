# 二叉搜索树节点
class BSTNode:

    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0
        self.word = None


# 二叉搜索树生成并统计
class BSTree:

    def __init__(self):
        self.root = None

    def Insert(self, input_word):
        node = BSTNode()
        node.word = input_word

        if self.root is None:
            self.root = node
            node.count += 1
        else:
            cur_node = self.root
            while True:
                if input_word < cur_node.word:
                    if cur_node.left: cur_node = cur_node.left
                    else:
                        cur_node.left = node
                        node.count += 1
                        break
                elif input_word > cur_node.word:
                    if cur_node.right: cur_node = cur_node.right
                    else:
                        cur_node.right = node
                        node.count += 1
                        break
                else:
                    cur_node.count += 1
                    break

    def input_text(self,text_src):
        fo = open(text_src, "r")
        text = fo.read()

        text = text.lower()
        for ch in text:
            if not ch.islower():
                text = text.replace(ch, ' ')
        wordList = text.split()

        for word in wordList:
            self.Insert(word)

        fo.close()

    def MidOrder(self, node):
        if node is None: return
        else:
            self.MidOrder(node.left)
            self.stat[node.word] = node.count
            self.MidOrder(node.right)

    def output(self):
        self.stat = {}
        self.MidOrder(self.root)
        return self.stat


# 统计字符串文本中各单词（不区分大小写）出现的次数
# 使用字典实现，统计信息以[单词：频数]的字典进行保存
# 基于二叉搜索树的构建实现单词频数的统计 输出结果已排序 时间复杂度为 O(n*logn)

def BST_word_count(text_src):
    bst = BSTree()
    bst.input_text(text_src)
    return bst.output()


# print(BST_word_count("./essay_text.txt"))
