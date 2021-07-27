
def program():
    try:
        name = input("이름을 입력하세요 : ")
        score = int(input("점수를 입력하세요 : "))

        def grader(name, score):
            if 100 >= score >= 95:
                grade = "A+"
            elif 95 > score >= 90:
                grade = "A"
            elif 90 > score >= 85:
                grade = "B+"
            elif 85 > score >= 80:
                grade = "B"
            elif 80 > score >= 75:
                grade = "C+"
            elif 75 > score >= 70:
                grade = "C"
            elif 70 > score >= 65:
                grade = "D+"
            elif 65 > score >= 60:
                grade = "D"
            elif 60 > score:
                grage = "F"
            else:
                print("Error")
                name = input("이름을 입력하세요 : ")
                score = int(input("점수를 입력하세요: "))
                grader(name, score)
            print("학생이름 : ", name,
                  "\n점수 : ", score,
                  "\n학점 : ", grade)
        grader(name, score)
    except:
        print("Error, please enter numeric input")
        program()

program()