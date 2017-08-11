## 1주차 과제 1 - 맛집 고르기

# 구현 내용
# 실행시 한식, 중식, 일식 중 한 가지를 선택
# 선택하면 해당하는 분류에 속하는 식당을 임의로 하나 추천해줍니다.

list_koreanfood = ["부산국밥", "전주비빔밥", "춘천닭갈비"]
list_chinesefood = ["홍콩반점", "서울반점", "용왕루"]
list_japanesefood = ["돈부리", "라멘", "스시"]

print("한식, 중식, 일식 중 하나를 골라 입력하세요.")
food = input("입력 :")

import random

if food == "한식":
    rand_item = random.choice(list_koreanfood)
    print("추천 맛집 : " + rand_item)

elif food == "중식":
    rand_item = random.choice(list_chinesefood)
    print("추천 맛집 : " + rand_item)

elif food == "일식":
    rand_item = random.choice(list_japanesefood)
    print("추천 맛집 : " + rand_item)

else:
    print("입력 오류 발생, 프로그램을 다시 실행시켜주세요.")
