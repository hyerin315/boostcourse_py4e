import random

while 1:
    try:
        games = int(input("몇 판을 진행하시겠습니까? : "))

        if games < 1:
            print('1 이상의 숫자를 입력해주세요')
            continue

        break
    except Exception:
        print('숫자만 입력하세요')

def rcp(user, com):
    myNumber = -1

    if user in vaildInput: #user in 가위/바위/보
        myNumber = vaildInput[user]
    else:
        myNumber = int(user) #user in 0/1/2
        user = list(vaildInput.keys())[myNumber]

    comNumber = vaildInput[com]

    print('나 : ', user, '\n컴퓨터 : ', com)
    result = ''

    if comNumber - myNumber == 0:
        myResult['무'] += 1
        comResult['무'] += 1
        return '무승부!'
    elif (comNumber == 0 and myNumber == 2) or (comNumber - myNumber == 1):
        myResult['패'] += 1
        comResult['승'] += 1
        return '컴퓨터의 승리!'
    else:
        myResult['승'] += 1
        comResult['패'] += 1
        return '나의 승리!'

def sp_advanced(totalCnt):
    vaildInputKeys = vaildInput.keys()
    vaildInputValues = [ str(x) for x in vaildInput.values() ] #convert int to str

    for cnt in range(1, totalCnt + 1):
        while 1:
            try:
                #my input value
                my = input("\n가위 바위 보 : ")

                #예외 입력 체크
                if my not in vaildInput and my not in vaildInputValues:
                    print(', '.join(vaildInputKeys), ', ', ', '.join(vaildInputValues), ' 중 입력해주세요')
                    continue

                #computer random
                computer = random.choice(list(vaildInputKeys))

                result = rcp(my, computer)

                print(cnt, '번째 판 ', result)
                print("남은 기회는", totalCnt - cnt, "번입니다.\n")

                break
            except Exception as e:
                print(', '.join(vaildInputKeys), ', ', ', '.join(vaildInputValues), '중 입력해주세요')

    print('\n나의 전적 : ', myResult['승'],'승 ', myResult['무'],'무 ', myResult['패'],'패')
    print('컴퓨터의 전적 : ', comResult['승'],'승 ', comResult['무'],'무 ', comResult['패'],'패')

vaildInput = { '가위': 0, '바위': 1, '보': 2 }
myResult = { '승': 0, '무': 0, '패': 0 }
comResult = { '승': 0, '무': 0, '패': 0 }

sp_advanced(games)