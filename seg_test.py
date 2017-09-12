#-*-coding:utf-8-*-

import jieba.posseg as posseg
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os
from glob import glob

if len(sys.argv) != 3:
    print 'input parameter error'
    print 'e.g. python seg_test.py 1 ent'
    exit(0)

label = sys.argv[1]
classname = sys.argv[2]

inputpath = './training_set/'+label+'_'+classname+'/'+label+'_'+classname+'_texts'
#filename = 'text_'+str(count)+'.txt'
outputpath = 'seg_train/'+label+'_'+classname
#outputname = '/seg_text'+str(count)+'.txt'
pattern = re.compile('[v]*n.*')

if not os.path.exists(outputpath):
    os.makedirs(outputpath)

file_list = glob(inputpath+'/text_*.txt')
for inputname in file_list:
    print inputname
    fr = open(inputname,'r')
    outputname = inputname.replace(inputpath,outputpath)
    print outputname
    output = open(outputname,'w')
    for line in fr.readlines():
        #sentence = unicode(line.strip())
        sentence = line.strip()
        words = list(posseg.cut(sentence))
        #words = posseg.lcut(sentence) #可直接返回list
        for word in words:
            #print word.word,word.flag        
            if pattern.match(word.flag): #word.flag:词性
                #print word.word,word.flag
                output.write(word.word + '\t')
    fr.close()
    output.close()