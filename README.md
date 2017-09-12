# naive-bayes
#这是一个手动实现的朴素贝叶斯十分类代码

1、分词
对每个类别下的文件进行分词,使用jieba分词提取出名词词性的词(速度慢)
seg_test.py
2、去停用词
对每个类别下的文件进行去停用词操作
rmstopwords.py
3、生成词袋
将每个类别的文件进行整合后，生成该类别对应的词袋
integ.py bagwords.py
4、特征选择
为了方便计算idf值，创建了numofdocs.py
计算每个词的tf-idf值，选取具有代表性的词生成最终的词典:tfidf.py
选取特征作为最终词典:select.py
5、将训练集和测试集每个文档转换为对应向量（根据最终词典final_dict.txt）
doc2vec.py
6、计算似然度矩阵并保存
likelihood.py
7、分类器
使用朴素贝叶斯算法进行分类
伯努利模型：nb_bernoulli.py
多项式模型：nb_mul.py   √
8、准确率、召回率的计算
accurate.py
