import os


# 统计字符串文本中各单词（不区分大小写）出现的次数
# 使用字典实现，统计信息以[单词：频数]的字典进行保存
# 字典的底层实现是高度优化的哈希表 时间复杂度为 O(n)

class Dict(object):
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
                dict = {}.fromkeys(split_str, 0)

                for word in split_str:
                    dict[word] += 1

                return dict
        else:
            with open(filename, 'w', encoding='uft-8') as file:
                print('Create a new file named %s' % filename)

        return {}
