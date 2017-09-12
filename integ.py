#-*-coding:utf-8-*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
start = time.time()

if len(sys.argv) != 3:
    print 'input parameter error'
    print 'e.g. python integ.py 1 ent'
    exit(0)

label = sys.argv[1]
classname = sys.argv[2]

count = 1
#outputname = 'integ/'+classname+'.txt'
outputname = 'integ/'+classname+'_test.txt'
filename = 'rmstopword_test/'+label+'_'+classname+'/text'+str(count)+'.txt'
print filename
#filename = 'rmstopword_train/1_ent/text'+str(count)+'.txt'
#outputname = 'integ/ent.txt'
output = open(outputname,'w')
output.close()

while(count < 14110):
    if(os.path.isfile(filename)):
        fr = open(filename,'r')
        output = open(outputname,'a')
        for line in fr .readlines():
            output.write(line.strip())
        output.write('\n')
        #if count == 5:
        #    break
        count += 1
        filename = 'rmstopword_test/'+label+'_'+classname+'/text'+str(count)+'.txt'
        print filename
        fr.close()
        output.close()
    else:
        count += 1
        filename = 'rmstopword_test/'+label+'_'+classname+'/text'+str(count)+'.txt'
        print filename

finish = time.time()
print 'running time:',(finish - start)