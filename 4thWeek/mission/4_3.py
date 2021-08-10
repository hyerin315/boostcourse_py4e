guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def wrong_guest_book(guest_book):
    guest_book_save = open("./guest_book.txt", "w", encoding="UTF-8")
    guest_book_save.write(guest_book)
    guest_book_save.close()

    file = open("./guest_book.txt", "r")

    for line in file:
        list = line.split(",")
        name = list[0]
        phone_num = list[1].strip()

        if (len(phone_num) == 13) and (phone_num[:3] == "010") and (phone_num.count("-") == 2):
            continue
        else:
            print("잘못 쓴 사람 : {}".format(name))
            print("잘못 쓴 번호 : {}\n".format(phone_num))


wrong_guest_book(guest_book)