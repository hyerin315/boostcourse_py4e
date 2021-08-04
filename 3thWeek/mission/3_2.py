import random

print("# 가위바위보 #")
rcpValue = {'가위' : 1, '바위' : 2, '보' : 3}
rcpResult = ['승리했습니다', '비겼습니다', '졌습니다']

#1. 몇 판 진행할 지 (숫자가 아닌 경우 재입력)
while True:
    try:
        gameNum = int(input("몇 판 진행하시겠습니까? "))
        if gameNum > 0:
            break
        else:
            continue
    except Exception:
        print("숫자만 입력하세요")

#2. 게임 함수
def rcp(win=0, lose=0):
    print("\n게임시작!")

    #gameNum()만큼 게임 진행
    i = 1
    while i <= gameNum:

        #내가 낼 것이 '가위, 바위, 보'가 아닐 경우 재입력
        while True:
            try:
                print("")
                myRcp = rcpValue[input("가위, 바위, 보! (낼 것을 입력하세요) : ")]
                break
            except:
                print("가위, 바위, 보 중에서 입력하세요")

        #컴퓨터가 '가위, 바위, 보' 중에 랜덤으로 선택
        comRcp_k = random.choice(list(rcpValue.keys()))
        comRcp = rcpValue[comRcp_k]

        if myRcp == comRcp :
            print("컴퓨터 :", str(comRcp_k))
            print(str(rcpResult[1]))
            print("남은 기회는 "+str(gameNum - i)+"번입니다.")
        elif (myRcp == 1 and comRcp == 3) or (myRcp == 2 and comRcp == 1) or (myRcp == 2 and comRcp == 3):
            win += 1
            print("컴퓨터 :", str(comRcp_k))
            print(str(rcpResult[0]))
            print("남은 기회는 "+str(gameNum - i)+"번입니다.")
        else:
            lose += 1
            print("컴퓨터 :", str(comRcp_k))
            print(str(rcpResult[2]))
            print("남은 기회는 " + str(gameNum - i) + "번입니다. \n")

        i += 1

    print("\n게임 횟수 : " + str(gameNum) + "\n나의 승패 : " + str(win) + "번,  패배 :" + str(lose) + "번 \n")

rcp()
