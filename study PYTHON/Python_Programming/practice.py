# 5번

units = [''] + list('십백천')
nums = '일이삼사오육칠팔구'
bigunit = ['', '', '', '', '만', '', '', '', '억', '']
while True :
    userinput = input("숫자는?")
    n = int(userinput)
    inputlen = len(userinput)

    # 문자열을 3자리 단위로 끊기
    num1 = num2 = num3 = ""
    num3 = userinput[-3:]
    num2 = userinput[:-3]
    num1 = num2[:-3]
    num2 = num2[-3:]

    if num1:
        print(num1, ",", sep="", end="")
    if num2:
        print(num2, ",", sep="", end="")
    print(num3)

    # 위와 같은 결과를 간단히 만들기
    print(format(n, ','))

    result = []
    i = 0
    while n > 0 :
        r = n % 10
        n = n // 10
        if r == 1 and i % 4 != 0:   # 일단위를 제외하면 "일"을 표시하지 않는다.
            result.append(units[i % 4] + bigunit[i])
        elif r > 0:
            result.append(nums[r-1] + units[i%4]+bigunit[i])
        i += 1
    print("".join(result[::-1]))