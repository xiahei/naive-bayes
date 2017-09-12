#-*-coding:utf-8-*-
#去停用词

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import time

start = time.time()

print 'load stopwords dic...'
stopword = open('my_stopwords.txt','r')
#stopword = open('stop_words_ch.txt','r')
stopwords_dict = list()
for line in stopword.readlines():
    stopwords_dict.append(line.strip())
stopword.close()
print 'load stopwords dic finished...'

if len(sys.argv) != 4:
    print 'input parameter error'
    print 'e.g. python rmstopwords.py train 1 ent'

mode = sys.argv[1]
label = sys.argv[2]
classname = sys.argv[3]

count = 1
filename = './seg_'+mode+'/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'
print filename
outputname = 'rmstopword_'+mode+'/'+label+'_'+classname+'/text'+str(count)+'.txt'

while(count < 14410):
    if(os.path.isfile(filename)):
        fr = open(filename,'r')
        output = open(outputname,'w')
        for line in fr.readlines():
            words = line.strip().split('\t')
            for word in words:
                if word in stopwords_dict:
                    #print word
                    continue
                if word == ' ':
                    continue
                pattern = re.compile(u'[\u0030-\u0039]+')   #去字母和数字
                if pattern.match(word):
                    continue
                pattern = re.compile(u'[\u0041-\u005a,\u0061-\u007a]+')
                if pattern.match(word):
                    continue 
                output.write(word+'\t')
        fr.close()
        output.close()
        #if count == 2:
        #    break
        count += 1
        filename = './seg_'+mode+'/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'
        print filename
        outputname = 'rmstopword_'+mode+'/'+label+'_'+classname+'/text'+str(count)+'.txt'
    else:
        count += 1    
        filename = './seg_'+mode+'/'+label+'_'+classname+'/seg_text'+str(count)+'.txt'
        print filename
        outputname = 'rmstopword_'+mode+'/'+label+'_'+classname+'/text'+str(count)+'.txt'

finish = time.time()
print 'running time:',(finish-start)