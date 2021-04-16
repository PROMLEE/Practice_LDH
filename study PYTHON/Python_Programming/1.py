region = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
count = len(region)
yesterday = ['0']*count

def find_max(n):
    result = 0
    for i in range(len(n)):
        if int(n[i]) > int(result):
            result = n[i]
    return result

while True:
    today = input().split()
    # 잘못된 입력/종료 처리
    if today[0] == '-1':
        print("코로나 확진자 통계 프로그램을 종료합니다.")
        break
    elif len(today) != count:
        print("{}개의 데이터가 입력되었습니다.".format(len(today)))
        print("{}개의 데이터를 입력해주세요.".format(count))
        continue
    print("     ", " ".join(region))
    # 어제
    print("어제  ", end="")
    for i in range(count):
        print("%-5s" % yesterday[i], end="")
    # 오늘
    print("\n오늘  ", end="")
    today_max = find_max(today)
    for i in range(count):
        if today[i] == today_max:
            result = "(" + today[i] + ")"
            print("%-5s" % result, end="")
        else:
            print("%-5s" % today[i], end="")
    # 변동
    print("\n변동  ", end="")
    for i in range(count):
        change = int(today[i])-int(yesterday[i])
        change = str(change)
        if int(change) > 0:
            change = "+" + change
        print("%-5s" % change, end="")
    # 누계
    total = []
    print("\n누계  ", end="")
    for i in range(count):
        total_val = int(today[i])+int(yesterday[i])
        total.append(total_val)
    total_max = find_max(total)
    for i in range(count):
        if total[i] == total_max:
            result = "("+str(total[i])+")"
            print("%-5s" % result, end="")
        else:
            print("%-5d" % total[i], end="")
    print()
    yesterday = today
