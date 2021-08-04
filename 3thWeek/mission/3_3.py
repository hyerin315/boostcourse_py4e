
def inputValue():
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    return n, m


def find_even_number(x):
    n, m = x
    numbers = []

    while True :
        try:
            if n < m :
                break
        except:
            print("다시 입력하세요")
            inputValue()

    for i in range(n, m):
        numbers.append(i)

    for number in numbers:
        if number % 2 == 0:
            print(number, "짝수")
            try:
                if ((len(numbers) % 2) == 1) and (numbers[int(len(numbers) / 2 + 1)] == number) :
                    print(str(numbers[int(len(numbers) / 2 + 1)]), "중앙값")
            except:
                break

find_even_number(inputValue())