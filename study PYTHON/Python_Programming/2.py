while True:
    sentence = input('문장을 입력하세요: ').split()
    if sentence[0] == 'exit':
        print("프로그램을 종료합니다.")
        break
    name = 0
    if sentence[0] == '저는' and sentence[1][-3:] == '이라고':
        name = sentence[1].replace("이라고", "")
    elif sentence[0] == '제':
        name = sentence[2].replace("입니다.", "")
    else:
        name = sentence[1].replace("입니다.", "")
    print('이름:', name)
    print()
