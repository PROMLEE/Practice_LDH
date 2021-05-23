while True:
    try:
        file_name = input('성적이 저장된 파일명을 입력해주세요.\n')
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
        if overwrite == 'y': break
        else:
            while True:
                file_name2 = input('파일 이름을 다시 입력해주세요.\n')
                if file_name2[-4:] == '.txt': break
                else:
                    print('파일의 확장자를 .txt로 입력해주세요.')
                    continue
    except FileNotFoundError: break
f = open(file_name2, 'w',encoding='utf-8')
s = '%33s'%'성적표\n'
f.write(s)
s = '%7s'%'학번' + '      국어   영어  수학   총점     평균   석차\n'
f.write(s)
s='='*50 + '\n'
f.write(s)
for i in data:
    s = '  ' + i[0]
    for j in i[1:5]:
        s += '%7s'%str(j)
    s += str('%10.2f'%i[5])
    rank = score.index(i[4]) + 1
    s += '%6s'%str(rank)
    s += '\n'
    f.write(s)
f.close()
print(file_name2, '파일을 저장 성공했습니다.')
