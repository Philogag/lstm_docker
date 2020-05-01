import jieba
import pandas as pd
from collections import Counter

# 加载无意义词典
with open("./model/ignoreWords.txt") as f:
    ignoreWords = [s[:-1] for s in f.readlines()]

def split(data):
    data['cut'] = data['comment'].apply(lambda x: [i for i in jieba.cut(x) if i not in ignoreWords])
    return data

def worldcount(data):
    words = []

    for content in data['cut']:
        words.extend(content)

    # 创建分词数据框
    corpus = pd.DataFrame(words, columns=['word'])
    corpus["cnt"] = 1
    # 分组统计
    g = corpus.groupby(['word']).count()
    g.sort_values('cnt', ascending=False, inplace=True)
    return g


if __name__ == "__main__":
    data = {
        "comment": ["出门旅游拍拍风景是完全没有问题的，相信老爸一定会喜欢它的！", "非常喜欢"]
    }
    data = pd.DataFrame(data)
    count = worldcount(split(data))
    print(count.to_dict())
    

# print(ignoreWords[:10])