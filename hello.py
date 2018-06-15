
import csv

f = open('한국교육학술정보원_학교알리미_2017 입학생 현황(고)_20170928.csv')
file = csv.reader(f)
next(file)
data = []
for row in file:
    data.append(row)
    
region = []
gradm = []
gradf = []

for i in data:
    if i[0] == '서울특별시교육청' :    
        if i[2] not in region:
            region.append(i[2])
            gradm.append(0)
            gradf.append(0)
        
for i in data:
    for j in range(len(region)):
        if i[2] == region[j]:
            if i[10] != '':
                gradm[j] += int(i[10])
                
for i in data:
    for j in range(len(region)):
        if i[2] == region[j]:
            if i[11] != '':
                gradf[j] += int(i[11])               
            
final = []
for i in range(len(region)):
    final.append([region[i], gradm[i], gradf[i]])

pl1 = ''
pl2 = ''
pl3 = ''
pl4 = ''
pl5 = ''
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in final:
    if i[2] > n1:
        pl5 = pl4
        pl4 = pl3
        pl3 = pl2
        pl2 = pl1
        pl1 = i[0]
        n5 = n4
        n4 = n3
        n3 = n2
        n2 = n1
        n1 = i[1]
    elif i[2] > n2:
        pl5 = pl4
        pl4 = pl3
        pl3 = pl2
        pl2 = i[0] 
        n5 = n4
        n4 = n3
        n3 = n2
        n2 = i[1]
    elif i[2] > n3:
        pl5 = pl4
        pl4 = pl3
        pl3 = i[0]
        n5 = n4
        n4 = n3
        n3 = i[1]
    elif i[2] > n4:
        pl5 = pl4
        pl4 = i[0]     
        n5 = n4
        n4 = i[1]
    elif i[2] > n5:
        pl5 = i[0]
        n5 = i[1]

print (pl1, pl2, pl3, pl4, pl5)