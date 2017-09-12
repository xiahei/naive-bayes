#-*-coding:utf-8-*-

#假设每类先选取前500个作为关键词

label = ['ent','fin','spo','tec','mil','soc','lif','cul','car','hel']
output = open('final_dict.txt','w')
for l in label:
    filename = 'integ/'+l+'_tfidf.txt'
    fin = open(filename,'r')
    count = 0
    for line in fin.readlines():
        word = line.strip().split('\t')[0]
        output.write(word + '\n')
        count += 1
        if count == 500:
            break
    fin.close()
output.close()