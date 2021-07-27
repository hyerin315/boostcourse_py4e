import random

def game():
    print("가위 바위 보 시작! ")
    a = input("나 : ")
    b = random.randint(0,2)

    #가위 = 0, 바위 = 1, 보 = 2
    if a == '가위':
        a = 0
        if b == 0:
            print("컴퓨터 : 가위")
            return "Draw"
        elif b == 1:
            print("컴퓨터 : 바위")
            return "win"
        elif b == 2:
            print("컴퓨터 : 보")
            return "lose"
    elif a == '바위':
            a = 1
            if b == 0:
                print("컴퓨터 : 가위")
                return 'win'
            elif b == 1:
                print("컴퓨터 : 바위")
                return 'draw'
            elif b == 2:
                print("컴퓨터 : 보")
                return 'lose'
    elif a =='보' :
            a = 2
            if b == 0:
                print("컴퓨터 : 가위")
                return "lose"
            elif b == 1:
                print("컴퓨터 : 바위")
                return "win"
            elif b == 2:
                print("컴퓨터 : 보")
                return "draw"


print("결과 : ", game())



