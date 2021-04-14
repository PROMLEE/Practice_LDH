while True:
    sentence = input("수식을 입력하세요: ").split('+')
    if sentence[0] == "exit":
        print("프로그램을 종료합니다.")
        break

    plus = []
    minus = []
    result = 0
    for i in sentence:
        if '-' not in i:
            plus.append(i)
            sentence.remove(i)
    for i in sentence:
        a = i.split('-')
        plus.append(a[0])
        del a[0]
        for j in a:
            minus.append(j)
    
    for i in plus:
        result += int(i)
    for i in minus:
        result -= int(i)
    print("결과는",result)
