import random  # 랜덤 추출을 위함

dict_list = []
num = int(input('총 플레이어 수 입력: '))
i = 0

while True:
    i = i + 1
    if(i <= num):
        my_dict = {}  # empty dictionary
        key = int(input('플레이어 번호 입력 : '))
        val = input('이름 입력 : ')
        my_dict[key] = val
        dict_list.append(my_dict)
    else:
        break

print("플레이어 리스트 : ", dict_list)

block = ["ㄹ", "ㄱ", "ㄴ", "ㅁ", "ㅣ", "ㅜ"]
choiceList = random.choice(block)

print("당신의 블록: " + choiceList)


def check():
    print("1. 오른쪽 2. 왼쪽 3. 블록 바꾸기 4. 종료")

    number = int(input("숫자를 입력하세요 : "))

    print("당신이 입력한 숫자는 ? ", number)

    if number == 1:
        print("오른쪽으로 이동")
    elif number == 2:
        print("왼쪽으로 이동")
    elif number == 3:
        print("블록 변경!! 저장된 블록: " + choiceList)
    elif number == 4:
        print("종료")
        return
    else:
        print("잘못 눌렀어")
    check()  # 재귀함수로 반복


check()