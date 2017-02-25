#coding=utf-8
# 0004任一个英文的纯文本文件，统计其中的单词出现的个数

from collections import Counter
import re
def count(filepath):
    f = open(filepath,'rb')
    wdic={}
    for line in f:
        line = line.lower().strip()
        words = re.split('\W+',line)

        for word in words:
            if word in wdic:
                wdic[word]+=1
            else:
                wdic[word]=1
    f.close()
    wdic = sorted(wdic.items(),key = lambda x:x[1],reverse = True)
    print wdic

if __name__=='__main__':
    num = count('test.txt')

