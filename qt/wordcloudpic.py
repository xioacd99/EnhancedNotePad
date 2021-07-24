import time
import imageio
import requests
from wordcloud import WordCloud

url = 'http://top.baidu.com/region/singlelist'

'''
省份热搜词
'''
# 城市列表
list = [928, 934, 911, 904, 909, 913, 925, 912, 902, 920, 921, 927, 908, 906, 930, 922, 916, 903, 907, 905, 919, 918,
        910, 914, 901, 929, 924, 923, 931, 932, 933, 926, 915, 917, ]
result = {}
# 循环获取信息
for i in list:
    data = {
        'boardid': '2',
        'divids[]': i,
    }
    html = requests.post(url=url, data=data).json()
    x = str(i)
    data = html['topWords'][x]
    lists = {i['keyword']: i['searches'] for i in data}
    result.update(lists)
# pic为背景形状
Pic = imageio.imread('duck.png')
# 实例化词云
w = WordCloud(width=1000, height=700, font_path='simhei.ttf', background_color='white', mask=Pic, scale=15)
# 将爬取的数据给词云
w.fit_words(result)
# 将结果根据时间写到图片
now = time.strftime('%Y-%m-%d', time.localtime())
w.to_file(f'{now}resou.png')
