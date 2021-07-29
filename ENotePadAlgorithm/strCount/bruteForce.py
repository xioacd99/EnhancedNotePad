import os


# 统计字符串文本中各单词（不区分大小写）出现的次数
# 使用字典实现，统计信息以[单词：频数]的字典进行保存
# 直观的进行暴力法计数 在已记录过的单词中遍历 时间复杂度为 O(n^2)

class BruteForce(object):
    def fileCount(self, filename, caseSensitive=True):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                if not caseSensitive:
                    text = text.lower()
                for ch in text:
                    if not ch.islower():
                        text = text.replace(ch, ' ')
                split_str = text.split()

                words = []
                counts = []

                for word in split_str:
                    if word not in words:
                        words.append(word)
                        counts.append(1)
                    else:
                        for i in range(0, len(words)):
                            if words[i] == word:
                                counts[i] += 1

                dict = {}
                for i in range(0, len(words)):
                    dict[words[i]] = counts[i]
                return dict
        else:
            with open(filename, 'w', encoding='uft-8') as file:
                print('Create a new file named %s' % filename)
        return {}
