#-*-coding:utf-8-*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from glob import glob

import time
start = time.time()

if len(sys.argv) != 3:
    print 'input parameter error'
    print 'e.g. python integ.py 1 ent'
    exit(0)

label = sys.argv[1]
classname = sys.argv[2]

outputpath = 'integ/'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
outputname = 'integ/'+classname+'.txt'
output = open(outputname,'w')

inputpath = 'rmstopword_train/'+label+'_'+classname
file_list = glob(inputpath+'/text_*.txt')
for inputname in file_list:
    print inputname
    fr = open(inputname,'r')
    for line in fr.readlines():
        output.write(line.strip())
    output.write('\n')
output.close()

finish = time.time()
print 'running time:',(finish - start)