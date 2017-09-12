#-*-coding:utf-8-*-

from numpy import *

def accuracy(actual,pred):
    accurate = 0
    actual = array(actual)
    pred = array(pred)
    m = shape(actual)[0]
    #print 'm:',m
    count = m
    for i in range(m):
        if actual[i] == pred[i]:
            accurate += 1
    accuracy = float(accurate) / count
    print 'accuracy:',accuracy

#正确率P = TP/(TP+FP) ;  反映了被分类器判定的正例中真正的正例样本的比重 
#R = TP/(TP+FN) = 1 - FN/T;  反映了被正确判定的正例占总的正例的比重 
#针对每个类别分别做处理
def precision(actual,pred,label):
    true = 0 #被判定为正例的所有样例数
    actual_true = 0 #被判定为正例本身也是正例的样例数
    actual = array(actual)
    pred = array(pred)
    m = shape(actual)[0]
    for i in range(m):
        #print pred[i]
        #print label
        if pred[i] == str(label):
            true += 1
            #print true
        if (pred[i] == actual[i]) and (actual[i] == str(label)):
            actual_true += 1
            #print actual_true
    pre = float(actual_true)/true
    print '%d_precison:%s' %(label,pre)
    return pre

def recall(actual,pred,label):
    actual_true = 0 #被判定为正例本身也是正例的样例数
    true = 0  #所有为正例的样例数
    actual = array(actual)
    pred = array(pred)
    m = shape(actual)[0]
    for i in range(m):
        if actual[i] == str(label):
            true += 1
        if (pred[i] == actual[i]) and (actual[i] == str(label)):
            actual_true += 1 
    rec = float(actual_true)/true
    print '%d_recall:%s'%(label,rec)
    return rec

actual = open('actual.txt','r')
target = []
for line in actual.readlines():
    target.append(line.strip())
y_actual = array(target)

pred = open('result_mul.txt','r')
test_target = []
for line in pred.readlines():
    test_target.append(line.strip())
y_pred = array(test_target)

accuracy(y_actual,y_pred)
pre = 0.0
rec = 0.0
for i in range(10):
    label = i + 1
    #label = 1
    pre += precision(y_actual,y_pred,label)
    rec += recall(y_actual,y_pred,label)
print 'total precision:',float(pre)/10
print 'total recall:',float(rec)/10
    