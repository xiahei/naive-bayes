#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 2:
    print 'input parameter error'
    print 'e.g. python doc2vec.py ent'
    exit(0)

classname = sys.argv[1]

import time
start = time.time()
#加载最终生成的词典
print 'load final dict...'
final_dict = list()
fin = open('final_dict.txt','r')     
for line in fin.readlines():
    final_dict.append(line.strip())
fin.close()
print 'finish loading...'

#multinomial对应向量
filename = 'integ/' + classname + '.txt'
outputname = 'vec/'+classname+'.txt'
#filename = 'integ/' + classname + '_test.txt'
#outputname = 'vec/'+classname+'_test.txt'
fr = open(filename,'r')
output = open(outputname,'w')
vector = [0] * len(final_dict)
for line in fr.readlines():
    words = line.strip().split('\t')
    for word in words:
        if word in final_dict:
            vector[final_dict.index(word)] += 1
    for i in range(len(vector)):
        output.write(str(vector[i]) + '\t')
    output.write('\n')

finish = time.time()
print 'running time:',(finish - start)