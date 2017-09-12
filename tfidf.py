#-*-coding:utf-8-*-

#feature selection
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 2:
    print 'input parameter error'
    print 'e.g. python tfidf.py ent'

import math
classname = sys.argv[1]

import time 
start = time.time()

#tf*idf：如果某个词在某一类中出现的频率高，但在其他类中很少出现，则该词具有较好的类别区分能力

#tf  词频 = 某个词在文章中出现的总次数/文章的总词数
#这边计算了每个类中每个词的词频，而不是对应的文档中
inputname = 'integ/'+classname+'_bag.txt'   #'integ/ent_bag.txt'
fr = open(inputname,'r')
whole_count = 0
num = 0
for line in fr.readlines():    
    count = line.strip().split('\t')[-1]
    #print count
    whole_count += int(count)
    #num += 1
    #if num == 90000:
    #    break
print 'whole_count:',whole_count
fr.close()

print 'tf start..'
#输出为对应tf文档
outputname = 'integ/'+classname+'_tf.txt'
fr = open(inputname,'r')
output = open(outputname,'w')
for line in fr.readlines():
    count = line.strip().split('\t')[-1]
    word = line.strip().split('\t')[0]
    tf = float(count) / whole_count
    #print tf
    #num += 1
    #if num == 10:
    #    break
    output.write(word + '\t' + str(tf) +'\n')

fr.close()
output.close()
print 'tf finished'

#idf = log(文档总数/包含该词的文档数)
doc_num = 113673 #文档总数
#十个类词集保存至内存
#label = ['ent','fin','spo','tec','mil','soc','lif','cul','car','hel']
label = ['ent']
print 'load list...'
word_dict = {}
for c in label:
    filename = 'integ/'+c+'_list.txt'
    fin = open(filename,'r')
    for line in fin.readlines():
        word = line.strip().split('\t')[0]
        count = line.strip().split('\t')[-1]
        if word in word_dict:
            word_dict[word] += int(count)
        else:
            word_dict[word] = int(count)
    fin.close()
#计算idf值
fr = open(inputname,'r')
outputidf = 'integ/'+classname+'_idf.txt'
output = open(outputidf,'w')
doc_cnt = 0.0
print 'idf start...'
for line in fr.readlines():
    word = line.strip().split('\t')[0]
    if word in word_dict:
        doc_cnt = word_dict[word]
    idf = math.log(float(doc_num)/doc_cnt)
    output.write(word + '\t' + str(idf) + '\n')
fr.close()
output.close()
print 'idf finished'

#tf-idf
print 'tf-idf start...'
tf = 'integ/'+classname+'_tf.txt'
idf = 'integ/'+classname+'_idf.txt'
fin_tf = open(tf,'r')
fin_idf = open(idf,'r')

tfidf_dict = dict() 
for line in fin_tf.readlines():
    word = line.strip().split('\t')[0]
    tf_value = line.strip().split('\t')[-1]
    tfidf_dict[word] = tf_value
fin_tf.close()

for line in fin_idf.readlines():
    idf_value = line.strip().split('\t')[-1]
    word = line.strip().split('\t')[0]
    if word in tfidf_dict:
        tfidf_dict[word] = float(tfidf_dict[word]) * float(idf_value)
fin_idf.close()

tf_idf = sorted(tfidf_dict.iteritems(),key = lambda x : x[1],reverse = True)
fout_name = 'integ/'+classname+'_tfidf.txt'
fout = open(fout_name,'w')
for word,count in tf_idf:
    fout.write(word + '\t' + str(count) + '\n')
fout.close()
print 'tf-idf finished'

finish = time.time()
print 'running time:',(finish - start)