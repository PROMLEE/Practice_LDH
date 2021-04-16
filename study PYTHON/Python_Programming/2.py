from random import randint
def lotto_generator():
    numbers=[]
    for i in range(6):
        numbers.append(randint(1,45))
    return numbers

a = int(input("몇 번째 로또 번호를 고를까요?"))
for i in range(a):
    selectednum = lotto_generator()
    print(i,"회 : ",selectednum)
    # 앞쪽 로또 번호는 버리고 마지막 로또 번호만 남는다.

print("이번 주의 로또 번호입니다.", end = "")
for i in selectednum:
    print(i, end=" ")