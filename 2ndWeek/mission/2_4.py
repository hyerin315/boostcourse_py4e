inputAge = int(input('나이를 입력하세요.'))
inputType = input('지불유형을 입력하세요. (카드/현금)')
def bus_fare(age, type):
    fareList = {
        '8세 미만': '무료',
        '8세 이상 - 14세 미만': { '카드': '450원', '현금': '450원' },
        '14세 이상 - 20세 미만': { '카드': '720원', '현금': '1000원' },
        '20세 이상': { '카드': '1200원', '현금': '1300원' },
        '75세 이상': '무료',
    }
    fare = ''
    if age < 8 or age >= 75:
        fare = fareList['8세 미만']
    elif age >= 8 and age < 14:
        fare = fareList['8세 이상 - 14세 미만'][type]
    elif age >= 14 and age < 20:
        fare = fareList['14세 이상 - 20세 미만'][type]
    elif age >= 20:
        fare = fareList['20세 이상'][type]
    else:
        fare = fareList['75세 이상']
    print('\n나이 : ', age, '\n지불유형 : ', type, '\n버스요금 : ', fare)

bus_fare(inputAge, inputType)