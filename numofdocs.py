#-*-coding:utf-8-*-

#用于idf的计算

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time

start = time.time()
word_dict = dict()

classname = ['ent']
#classname = ['ent','fin','spo','tec','mil','soc','lif','cul','car','hel']
for name in classname:
    filename = 'integ/'+name+'.txt'
    fr = open(filename,'r')
    for line in fr.readlines():
        words = line.strip().split('\t')
        word_list = set()     #去每个文档的重复词
        for word in words:
            word_list.add(word)
        for word in word_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    fr.close()
    #sorted(iterable,cmp=None,key=None,reverse=False)
    w = sorted(word_dict.iteritems(),key = lambda x : x[1],reverse = True)
    outputname = 'integ/'+name+'_list.txt'
    output = open(outputname,'w')
    for word,count in w:
        output.write(word+'\t'+str(count)+'\n')

    output.close()

finish = time.time()
print 'running time:',(finish-start)