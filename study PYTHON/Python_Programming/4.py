phone={
    "홍길동":"010-4444-5555",
    "김중앙":"010-9191-8181",
    "심청":"010-3232-5454"
}
while True:
    n = input("이름>> ")
    if n == "exit":
        print("전화번호부를 종료합니다.")
        break

    if n == "add":
        a = input("이름은? ")
        b = input("전화번호는? ")
        phone[a]=b
        print(a,"전화번호가 추가되었습니다.")
    else:
        name = list(phone.keys())
        result = -1
        for i in range(len(name)):
            if n in name[i]:
                result = i
                number = phone[name[result]]
                print(name[result],"\t",number)
        if result == -1:
            print("찾을 수 없습니다.")