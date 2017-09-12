#-*-coding:utf-8-*-

import jieba.posseg as posseg
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os

if len(sys.argv) != 3:
    print 'input parameter error'
    print 'e.g. python seg_test.py 1 ent'
    exit(0)

label = sys.argv[1]
classname = sys.argv[2]

count = 1
filename = './training_set/'+label+'_'+classname+'/'+label+'_'+classname+'_texts/text_'+str(count)+'.txt'
outputname = 'seg_train/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'
pattern = re.compile('[v]*n.*')

while(count < 14110):
    if(os.path.isfile(filename)):
        fr = open(filename,'r')
        output = open(outputname,'w')
        for line in fr.readlines():
            #sentence = unicode(line.strip())
            sentence = line.strip()
            words = list(posseg.cut(sentence))
            for word in words:
                #print word.word,word.flag        
                if pattern.match(word.flag):
                    #print word.word,word.flag
                    output.write(word.word + '\t')
        fr.close()
        output.close()
        print count
        count += 1
        filename = './training_set/'+label+'_'+classname+'/'+label+'_'+classname+'_texts/text_'+str(count)+'.txt'
        outputname = 'seg_train/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'
    else:
        count += 1
        filename = './training_set/'+label+'_'+classname+'/'+label+'_'+classname+'_texts/text_'+str(count)+'.txt'
        outputname = 'seg_train/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'