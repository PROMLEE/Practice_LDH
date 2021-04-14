while True:
    n = input("숫자는? ")

    if n == "exit":
        print("프로그램이 종료되었습니다.")
        break

    # 입력받은 숫자를 문자열 리스트 a로 변환
    a = []
    for i in n:
        a.append(i)
    l = len(a)
    a.reverse()

    # 천단위 , 표시
    result = []
    for i in range(l):
        if i % 3 ==0 and i > 0:
            result.insert(0,',')
        result.insert(0, a[i])
    print("".join(result))

    # 한글로 표시
    num_kor = {'0': '', '1': '', '2': '이', '3': '삼', '4': '사',
            '5': '오', '6': '육', '7': '칠', '8': '팔', '9': '구'}
    kor1 = ('', '십', '백', '천')
    kor2 = ('', '만', '억', '조', '경', '해')
    result = []
    for i in range(l):
        # kor2
        if i % 4 == 0:
            if i+3 < l and a[i:i+4] == ['0', '0', '0', '0']:
                continue
            else:
                result.insert(0, kor2[i//4])
            if a[i] == '1' and (i != 4 or i+1 <l):
                result.insert(0, '일')
        # kor1
        if a[i] != '0':
            result.insert(0, kor1[i % 4])
        # num_kor
        result.insert(0, num_kor[a[i]])
    if n == "0":
        result.append("영")
    else:
        print("".join(result))
    print()
