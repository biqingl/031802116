import jieba
import numpy as np
import jieba.analyse
import os
import re
import sys
import math


# 命令行获取绝对路径
path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]

def read_txt(content):
    
    #读入原文本与抄袭文本
    doc=open(content,'r',encoding="utf-8")
    r = '[’!"#$%&\'()*+,-.<=>?@[\\]^_`{|}~\n。！， ]+'
    text = doc.read()
    text = re.sub(r,' ',word)
    doc.close()
    return text

def print_txt():
    sim=get_similarity(path1,path2)
    print(sim)
    #以字符串形式写入
    ans=("%.2f"%sim)
    temp_txt = open(path3,'w',encoding='utf-8')
    temp_txt.write(str(ans))
    temp_txt.close()
   
def get_similiarity(content1,content2):
    

    # 分词
    words1 = jieba.cut(content1)
    words2 = jieba.cut(content2)
    content_word1 = (','.join(words1)).split(',')
    content_word2 = (','.join(words2)).split(',')

    # 列出所有的词,取并集
    words_key = list(set(content_word1 + content_word2))
    
    
    
    # 给定形状和类型的用0填充的矩阵存储向量
    vect1 = np.zeros(len(words_key))
    vect2 = np.zeros(len(words_key))

    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(words_key)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(content_word1)):
            if words_key[i] == content_word1[j]:
                vect1[i] += 1
        for k in range(len(content_word2)):
            if words_key[i] == content_word2[k]:
                vect2[i] += 1      

     # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vect1)):
        sum += vect1[i] * vect2[i]
        sq1 += pow(vect1[i], 2)
        sq2 += pow(vect2[i], 2)
    try:
        similiarity = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        similiarity = 0.0
    return similiarity

    
if __name__ == '__main__':
    
    print_txt()

