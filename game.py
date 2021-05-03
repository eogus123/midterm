print("테트리스 시작")
list_a = ("1. 오른쪽", "2. 왼쪽", "3. 블럭 바꾸기", "4. 종료")
print(list_a)
dict_a = {1 : list_a[0],2 : list_a[1],3 : list_a[2],4 : list_a[3]}
num = int(input("선택 : "))
if num ==1:
    print(dict_a[1])
elif num == 2:
    print(dict_a[2])
elif num == 3:
    print(dict_a[3])
elif num == 4:
    print(dict_a[4])
else :
    print("숫자를 입력하세요.")