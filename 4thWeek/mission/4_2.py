def count_word():
    text = input("글을 복사, 붙여넣기 해주세요\n")
    word = input("카운팅할 글자를 적어주세요\n")

    #텍스트 저장
    textSave = open("./text01.txt", "w", encoding="UTF-8")
    textSave.write(text)
    textSave.close()

    count = 0
    textFile = open("./text01.txt", "r")
    textLines = textFile.readlines()
    for line in textLines:
        if word in line:
            count += line.count(word)
        elif word not in line:
            print("입력한 단어가 없습니다. 다시 입력해주세요\n")
            count_word()
    print(count)

count_word()
