# 연수가 4로 나누어떨어지면 윤년
# 연수가 100으로 나누어떨어지면 평년
# 연수가 400으로 나누어떨어지면 윤년
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def count_day(month, year):
    #윤년이면 2월은 29일
    if month == 2 and leap_year(year) == True:
        day= 29
    elif month == 2:
        day= 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day= 31
    else:
        day= 30
    return day


while True:
    n = input("달력? ").split()
    if n[0]=='-1':
        print("달력 프로그램을 종료합니다.")
        break
    year = int(n[0])
    month = int(n[1])
    print("SUN", "MON", "TUE", "WED", "TUR", "FRI", "SAT")
    day = 0
    for i in range(1921, year):
        if leap_year(i):
            day += 366
        else:
            day += 365

    for i in range(1, month):
        day += count_day(i, year)
    day += 1
    day_of_week = day % 7  # 0->금/ 6->목
    space = (day_of_week + 5) % 7
    for _ in range(space):
        print("   ", end=" ")
    for i in range(1, count_day(month, year)+1):
        print("%3d"%i, end=" ")
        if (space + i) %7==0:
            print()
    print("\n")