#-*-coding:utf-8-*-

#词袋模型
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 2:
    print 'input parameter error'
    print 'e.g. python bagwords.py ent'
    exit(0)

classname = sys.argv[1]

word_dict = dict()

filename = 'integ/'+classname+'.txt'
#filename = 'rmstopword_train/1_ent/text1.txt'
fr = open(filename,'r')
for line in fr.readlines():
    words = line.strip().split('\t')
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
fr.close()

#sorted(iterable,cmp=None,key=None,reverse=False)
w = sorted(word_dict.iteritems(),key = lambda x : x[1],reverse = True)
outputname = 'integ/'+classname+'_bag.txt'
output = open(outputname,'w')
for word,count in w:
    output.write(word+'\t'+str(count)+'\n')

output.close()