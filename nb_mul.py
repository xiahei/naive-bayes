#-*-coding:utf-8-*-

from numpy import *
import time

#p(wj | yi) = (类别yi下wj出现的总次数+1)/(类别yi下所有特征出现的总次数+|V|)
#返回每一类的似然度矩阵   

print 'loading...'
likelihood = loadtxt('vec/likelihood.txt',dtype = float32)
p_prior = 500.0/5000
def test(label):
    testfile = 'vec/'+label+'_test.txt'
    testmat = loadtxt(testfile,dtype = int16)
    #print testmat
    #print shape(testmat)
    count = 0
    doc_num,fea_num =  shape(testmat)
    output = open('result_mul.txt','w')
    for i in range(doc_num):
        result = []
        for j in range(10):
            p = sum(testmat[i] * likelihood[j]) + log(p_prior)
            result.append(p)
        print result
        label = result.index(max(result)) + 1
        output.write(str(label)+'\n')
        #if count == 10:
        #    break
        #count += 1
    output.close()

start = time.time()
classname = ['ent','fin','spo','tec','mil','soc','lif','cul','car','hel']
#classname = ['ent']
for label in classname:
    test(label)
finish = time.time()
print 'running time:',(finish - start)