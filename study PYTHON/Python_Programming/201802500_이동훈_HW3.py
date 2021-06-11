import matplotlib.pyplot as plt
import numpy as np
f = open('Weather.csv','r')
province = []
date = []
result = []
head_line = True
while True:
    v = f.readline()
    v = v[:-1]
    if head_line:
        head_line = False
        continue
    if v == '': break
    s = v.split(',')
    if s[1] not in province:
        province.append(s[1])
        date.append([])
        result.append([])
    x = province.index(s[1])
    if s[2][:7] not in date[x]:
        date[x].append(s[2][:7])
        result[x].append([0,0,0])
    y = date[x].index(s[2][:7])
    result[x][y][0] += float(s[3])
    result[x][y][1] += float(s[6])
    result[x][y][2] += 1
f.close()

print('도시 목록입니다.')
print('0 : ALL')
for i in range(len(province)):
    print('%-23s'%(str(i+1)+' : '+province[i]),end='')
    if i %2 == 1:
        print()
    if i == (len(province)-1):
        print()
user = int(input('도시의 번호를 고르세요. '))
user-=1

x = []
y = []
if user == -1:
    title = 'ALL'
    for i in range(len(date[0])):
        ptemp = 0
        count = 0
        for j in range(len(date)):
            ptemp += result[j][i][0]
            count += result[j][i][2]
        year = date[0][i][:4]
        month = date[0][i][5:]
        x.append(year+'-'+month)
        y.append(float('%.1f'%(ptemp/count)))
else:
    title = province[user]
    for i in range(len(date[user])):
        year = date[user][i][:4]
        month = date[user][i][5:]
        p = result[user][i]
        x.append(year+'-'+month)
        y.append(float('%.1f'%(p[0]/p[2])))
plt.figure(figsize=(14,9))
markers, stemlines, baseline = plt.stem(x, y)
markers.set_color('r')
stemlines.set_color('b')
stemlines.set_linewidth(0.8)
plt.yticks(list(range(int(min(y))-3,int(max(y))+3,1)))
plt.grid(True)
plt.title(title +' Monthly temperature',fontsize = 25, color = 'g')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.xticks(rotation=90)
plt.show()