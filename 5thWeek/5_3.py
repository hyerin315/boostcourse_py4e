import random


def guess_number():
    count = 0           # N차 시도, N값
    success = 3         # 랜덤 값이 3개임으로, 3번 성공할시 게임 종료
    com_numbers = []    # 컴퓨터 랜덤 값이 저장될 list
    my_numbers = []     # 내가 입력한 숫자 list
    answer = []         # 맞춘 랜덤 값 저장

    # 컴퓨터 랜덤 숫자 생성
    for i in range(3):
        number = random.randint(1, 100)
        if number in com_numbers:
            continue
        else:
            com_numbers.append(number)

    com_numbers.sort() # 순서대로 정렬


    # 게임 시작
    while success > 0: # 3번의 성공이 끝날 때까지 반복
        count += 1 # N차 시도 카운트

        print(f"{count}차 시도")
        my = int(input("숫자를 예측해보세요 : "))

        # 내가 입력한 숫자 list 생성 구문
        if my not in my_numbers:
            my_numbers.append(my)

            # 내가 입력한 숫자가 정답일 때
            if my in com_numbers:
                success -= 1 # 성공 횟수 차감

                # 내가 입력한 숫자가 최소, 중간, 최대값 중 어떤 값인지 리턴
                if my == com_numbers[0]:
                    answer.append(com_numbers[0])
                    print(f"숫자를 맞추셨습니다! : {my}는 '최솟값'입니다!")
                elif my == com_numbers[1]:
                    answer.append(com_numbers[1])
                    print(f"숫자를 맞추셨습니다! : {my}는 '중간값'입니다!")
                else:
                    answer.append(com_numbers[2])
                    print(f"숫자를 맞추셨습니다! : {my}는 '최대값'입니다!")

            # 내가 입력한 숫자가 정답이 아닐때
            else:
                print(f"{my}는 없습니다")

                # 시도한 횟수가 5의 배수일 때
                if count % 5 == 0:
                    # 내가 최솟값/최대값을 맞춘 상태에 따라, 다른 힌트 제공
                    if com_numbers[0] in answer:
                        if my > com_numbers[2]:
                            print(f"최댓값은 {my}보다 작습니다")
                        else:
                            print(f"최댓값은 {my}보다 큽니다")
                    elif com_numbers[2] in answer:
                        if my > com_numbers[0]:
                            print(f"최솟값은 {my}보다 작습니다")
                        else:
                            print(f"최솟값은 {my}보다 큽니다")
                    # 만약 맞추지 않은 상태라면
                    else :
                        if count % 10 == 0:
                            if my > com_numbers[2]:
                                print(f"최댓값은 {my}보다 작습니다")
                            else:
                                print(f"최댓값은 {my}보다 큽니다")
                        else:
                            if my > com_numbers[0]:
                                print(f"최솟값은 {my}보다 작습니다")
                            else:
                                print(f"최솟값은 {my}보다 큽니다")

                # 5의 배수가 아닐때
                else:
                    continue

        else:
            print(f"{my}는 이미 예측에 사용된 숫자입니다")
            count -= 1

    print(f"게임종료! \n{count}차 시도만에 성공!")

print(guess_number())