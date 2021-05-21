import time
import random
max_score = 0
execute = True
while execute:
    score = 0
    print('구구단을 외자. 문제 출력 후 3초 이내에 입력하세요.\n')
    for i in range(10):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print('%d)'% (i+1), a, '*', b, '= ', end='')
        before = time.time()
        c = int(input())
        after = time.time()
        if c == -1:
            execute = False
            break
        time_use = after - before
        if time_use > 3:
            result = '(제한시간이 지났습니다.)'
        elif c == a * b:
            result = '(맞았습니다.)'
            score += 3000-int(time_use*1000)
        else:
            result = '(틀렸습니다.)'
        print(result, '%.3f' % time_use, '초 소요 : Score =', score)
        print()
    print('결과 점수 :',score)
    if score > max_score:
        max_score = score
        print('최고 기록 갱신')
    print()