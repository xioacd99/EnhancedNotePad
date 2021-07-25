# 统计字符串文本中各单词（不区分大小写）出现的次数
# 使用字典实现，统计信息以[单词：频数]的字典进行保存
# 字典的底层实现是高度优化的哈希表 时间复杂度为 O(n)

def Dict_word_count(text_src):
    fo = open(text_src, "r")
    text = fo.read()

    text = text.lower()
    for ch in text:
        if not ch.islower():
            text = text.replace(ch, ' ')

    split_str = text.split()
    dict = {}.fromkeys(split_str,0)
    for word in split_str: dict[word] += 1

    fo.close()
    return dict


# print(Dict_word_count("./essay_text.txt"))






