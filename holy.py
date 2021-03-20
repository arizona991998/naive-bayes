import csv
from collections import Counter

atas = []
bawah = []
datatrain = []
with open('TrainsetTugas1ML.csv') as csv_file:
    datatrain = list(csv.reader(csv_file))
    a = 0
    b = 0
    for row in datatrain:
        if row[8] == '>50K':
            a = a + 1
            for i in range(7):
                atas.append(row[i+1])
        elif row[8] == '<=50K':
            b = b + 1
            for i in range(7):
                bawah.append(row[i+1])

with open('TestsetTugas1ML.csv') as csv_file:
    datatest = list(csv.reader(csv_file))

    x = Counter(atas)
    y = Counter(bawah)


def apapun(kategori,nama):
    for i in range(len(kategori)):
        if nama == kategori[i][0]:
            return(kategori[i][1])


q = []
w = []

for i,j in x.items():
    q.append([i,j/a])
for i,j in y.items():
    w.append([i,j/b])

answah = []
for i in range(1,len(datatest)):
    p_richman = a/(a+b)
    p_misqueen = b/(a+b)
    for j in range(1,len(datatest[0])):
        ari = datatest[i][j]
        p_richman = p_richman * apapun(q,ari)
        p_misqueen = p_misqueen * apapun(w,ari)
    zona = p_richman/(p_richman+p_misqueen)
    zul = p_misqueen/(p_richman+p_misqueen)
    if zona > zul :
        answah.append('>50K')
    elif zul > zona :
        answah.append('<=50K')        
print(answah)  

with open('TebakanTugas1ML.csv','w', newline='') as csv_file:
    dodol = csv.writer(csv_file)

    for abangganteng in range(0,len(answah)):
        dodol.writerow([answah[abangganteng]])
    

