from random import randint
RSP = ("가위", "바위", "보")  # 각각 리스트 RSP의 인덱스에 일대일 대응
com_win = com_lose = 0  # 컴퓨터의 승수, 패수 변수
user_win = user_lose = 0  # 사용자의 승수, 패수 변수
count = 1  # 라운드 카운트
print("가위바위보 게임")
print("컴퓨터 : 0승 0패, 당신 : 0승 0패")
while com_win != 3 and user_win != 3:
    print("(라운드 {})".format(count))
    com = randint(0, 2)  # 컴퓨터가 0부터 2중 임의의 숫자를 고른다.
    print("컴퓨터가 결정했습니다.")
    n = input("무엇을 내시겠습니까? (가위, 바위, 보) ")
    user = RSP.index(n)
    if com == user:  # 컴퓨터와 사용자가 비기면
        print("비겼습니다.")
    elif (com+1) % 3 == user:  # 사용자가 이기면
        # 사용자가 이기는 경우의 수 3가지를 각각의 인덱스로 규칙을 찾아보면
        # (com, user): (0, 1), (1, 2), (2, 0)
        # com + 1을 3으로 나눈 나머지가 user이면 user_win + 1
        user_win += 1
        print("컴퓨터는 {0}, 당신은 {1}, 당신이 이겼습니다.".format(RSP[com], RSP[user]))
    else:  # 컴퓨터가 이기면
        com_win += 1
        print("컴퓨터는 {0}, 당신은 {1}, 컴퓨터가 이겼습니다.".format(RSP[com], RSP[user]))
    print("컴퓨터 : {0}승 {1}패, 당신 : {2}승 {3}패".format(
        com_win, com_lose, user_win, user_lose))
    count += 1

if com_win == 3:
    print("컴퓨터 승리")
else:
    print("사용자 승리")
