
import random

print("가위 바위 보를 시작합니다!")
print("")


print("0(가위), 1(바위), 2(보) 중에 하나를 입력해주세요!")
my = input("나 : ")

def rsp(my):
    #0~2 숫자를 랜덤으로 뽑는 코드
    computer = random.randint(0, 2)

    if my < computer :

        if my < computer :

            result = "컴퓨터 승리!"
        elif my == computer :
            result = "비겼습니다!"