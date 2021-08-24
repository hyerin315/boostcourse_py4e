import numpy as np

# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],
                  [2,3,4,3,1,2,0,3,2,5,7,2],
                  [1,3,0,3,3,4,5,6,7,2,2,1],
                  [3,2,9,2,3,5,6,6,4,6,9,9],
                  [8,7,7,5,6,7,5,8,8,6,10,9],
                  [7,8,4,9,5,10,3,3,2,2,1,3]]

def sales_management(names, records):
    member_dic = {}                                      # 전체 멤버 담을 딕셔너리

    for i in range(len(names)):                          # 이름 list 길이만큼 반복
        member_dic[names[i]] = np.mean(records[i])       # 멤버별 평균 실적 딕셔너리에 추가 (ex. {갑돌이 : 4.0})

    ranking = sorted(member_dic.items(), reverse=True, key=lambda item: item[1]) # 값 크기 내림차순으로 랭킹 매기기

    bonus_names = (ranking[0][0], ranking[1][0])         # 랭킹 1위 이름, 2위 이름 가져오기
    counsel_name = (ranking[4][0], ranking[5][0])        # 랭킹 5위 이름, 6위 이름 가져오기

    for names in bonus_names:                            # 보너스 명단에서 이름 가져오기
        if member_dic[names] >= 5 :                      # 평균 실적이 5이상인 경우 출력
            print(f"보너스 대상자 : {names}")
        else:                                            # 평균 실적이 5미만인 경우 패스
            continue

    for names in counsel_name:                           # 면담 대상자 명단에서 이름 가져오기
        if member_dic[names] > 3:                        # 평균 실적이 3보다 높은 경우 패스
            continue
        else:                                            # 3보다 적은 경우 출력
            print(f"\n보너스 대상자 : {names}")



sales_management(member_names, member_records)

