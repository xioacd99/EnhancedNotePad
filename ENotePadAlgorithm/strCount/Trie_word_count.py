# 前缀树节点
class TrieNode:

    def __init__(self):
        self.word = False   # 遍历到次节点时是否是完整的单词
        self.child = {}     # 子节点字典 [字符：节点]
        self.count = 0      # 到此是完整单词的次数


# 前缀树生成并统计
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.stat = {}

    def Insert(self, word):
        cur = self.root

        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]

        if not cur.word:
            cur.count = 1
            cur.word = True
        else:
            cur.count += 1

        self.stat[word] = cur.count

    def Trie_output(self):
        return self.stat
    
    def Trie_input(self, text_src):
        fo = open(text_src, "r")
        text = fo.read()
        
        text = text.lower()
        for ch in text:
            if not ch.islower():
                text = text.replace(ch,' ')
        wordList = text.split()

        for word in wordList:
            self.Insert(word)
        
        fo.close()


# 统计字符串文本中各单词（不区分大小写）出现的次数
# 使用前缀树实现，统计信息以[单词：频数]的字典进行保存
# 时间复杂度为 O(n*m) 其中n为单词数，m为单词的平均长度

def Trie_word_count(text_src):
    t = Trie()
    t.Trie_input(text_src)
    return t.Trie_output()


# print(Trie_word_count("./essay_text.txt"))

