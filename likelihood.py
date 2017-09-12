#-*-coding:utf-8-*-

#计算每一类中每个词在生成字典下的似然度
#利用Numpy矩阵进行运算
#p(wj | yi) = (类别yi下wj出现的总次数+1)/(类别yi下所有特征出现的总次数+|V|)
from numpy import *
v_num = 5000    #字典长度
m = (10,5000)
p_likelihood = zeros(m)
#p_likelihood = 
for j in range(10):
    label = j + 1
    trainfile = 'vec/'+str(label)+'.txt'
    trainmat = loadtxt(trainfile,dtype = int16) # turn to numpy.array
    #print 'trainmat'
    doc_num,fea_num = shape(trainmat)
    print doc_num,fea_num
    p = zeros(fea_num)
    p_sum = 0.0
    for i in range(doc_num):
        p += trainmat[i]                      #shape = 1* fea_num
        p_sum += sum(trainmat[i])
    p_likelihood[j] = log((p+ones(fea_num))/(p_sum+v_num))  #直接使用Numpy中的log函数
    #print shape(p_likelihood[j])
savetxt('vec/likelihood.txt',p_likelihood)