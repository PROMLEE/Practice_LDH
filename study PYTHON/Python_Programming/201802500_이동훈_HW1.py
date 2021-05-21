while True:
    try:
        file_name = input()
        f = open(file_name, 'r')
        break
    except FileNotFoundError:
        print('잘못된 파일명입니다. 다시 입력해주세요.')
        continue
data = []
score = []
for i in range(1,11):
    v = f.readline()
    if v == '':
        break
    if i !=10:
        v = v[:-1]
    s = v.split(',')
    s.append(int(s[1])+int(s[2])+int(s[3]))
    s.append(int(s[4])/3)
    score.append(s[4])
    data.append(s)
score.sort()
score.reverse()
data.sort()
f.close()
file_name2 = 'report.txt'
while True:
    try:
        f = open(file_name2, 'r')
        f.close()
        print(file_name2, '해당 파일을 덮어쓸까요? [y/n]')
        overwrite = input()
        if overwrite == 'y':
            break
        else:
            file_name2 = input('파일 이름을 다시 입력해주세요.\n')
    except FileNotFoundError:
        break
f = open(file_name2, 'w',encoding='utf-8')
s = '%25s'%'성적표\n'
f.write(s)
s = '%5s'%'학번' + '      국어  영어  수학  총점    평균    석차\n'
f.write(s)
s='='*50 + '\n'
f.write(s)
for i in data:
    s = i[0]
    for j in i[1:5]:
        s += '%6s'%str(j)
    s += str('%9.2f'%i[5])
    rank = score.index(i[4]) + 1
    s += '%6s'%str(rank)
    s += '\n'
    f.write(s)
f.close()
