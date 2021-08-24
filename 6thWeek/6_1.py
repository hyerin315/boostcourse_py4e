korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

def king(korea_king, chosun_king):
    king_dict = {}                          # 왕을 분류해 담을 딕셔너리
    count = 0                               # 중복되는 왕 이름 카운팅

    korea = korea_king.split(",")           # ','로 분리하기
    chosun = chosun_king.split(",")         # ','로 분리하기

    for ko in korea:                        # 고려왕 딕셔너리에 담기
        king_dict[ko] = 1                   # 고려왕들의 value값 : 1

    for cho in chosun:                      # 조선왕 딕셔너리에 담기
        if cho in list(king_dict.keys()):   # 왕 딕셔너리에 이미 담긴 왕이라면
            king_dict[cho] = 0              # 중복된 왕의 value값 : 0
            count += 1                      # 카운팅
        else:
            king_dict[cho] = 2              # 조선에만 있는 왕이라면 value값 : 2

    for key, value in king_dict.items():    # 출력문 : 왕 딕셔너리에서 key, value 가져오기
        if value == 0:                      # value가 0 이라면 출력
            print(f"조선과 고려에 모두 있는 왕 이름 : {key}")

    print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")
    print(king_dict)                        # 딕셔너리 구조 확인

king(korea_king, chosun_king)

