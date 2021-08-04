
print("구구단 시작! (홀수, 50이하 숫자만 출력합니다)")

def gugu():
    num = int(input("숫자를 입력하새요 : "))
    print("")
    if ((num % 2) == 1) and num <= 50:
        for i in range(1, 10):
            print(num, "*", i, "=", num * i)
    else :
        print("홀수/50이하 숫자가 아닙니다.")
        gugu()

gugu()