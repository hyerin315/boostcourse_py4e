my_id = input("주민등록번호를 입력해주세요 : ")

def check_id(my_id):
    #올바른 형식의 주민번호인지 체크
    if (my_id[6:7] == "-") and (len(my_id) == 14):
        id = my_id.split("-")

        birth = id[0].strip()
        unique = id[1].strip()
        my_gender = unique[:2]

        gender = ['남자', '여자']

        year = int(birth[:2])
        month = int(birth[2:4])

        #2000년대 이후 출생자인지 체크
        if year <= 0 and year <= 21 :
            birth_check = input("2000년대 이후 출생자입니까? 맞으면 o, 아니면 x : ").lower()

            if birth_check == "o":
                if my_gender == 3:
                    gender = gender[0]
                else:
                    gender = gender[1]
                print(f"{str(year).zfill(2)}월 {str(month).zfill(2)}일 {gender}")
            else:
                print("잘못된 번호 입니다.\n올바른 번호를 넣어주세요")
        else:
            if my_gender == 1:
                gender = gender[0]
            else:
                gender = gender[1]
            print(f"{str(year).zfill(2)}월 {str(month).zfill(2)}일 {gender}")

    else :
        print("잘못된 번호 입니다.")


check_id(my_id)