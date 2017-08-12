### 1주차 과제 3 - 가위 바위 보 게임

## 구현 내용
# 사용자에게 가위, 바위, 보 중 하나 입력받는다.
# 컴퓨터도 가위, 바위, 보를 내고 승패를 가른다.
# 3번을 지거나, 3번을 이기면 최종 스코어를 보여주며 종료

## 힌트
# 리스트는 1개를 사용하고 사용자의 입력을 받아야 한다.
# 임의 뽑기를 다시 사용한다.
# 가위, 바위, 보의 승패조건을 입력할 것

list_act = ["가위", "바위", "보"]

human_score = 0
com_score = 0

print("가위 바위 보 게임을 시작합니다.")
print(" ")

while True:
# while human_score == 3 or com_score == 3:
    print("무엇을 내시겠습니까?")
    human_act = input("입력 : ")
    import random
    com_act = random.choice(list_act)

    # 사용자 입력, 컴퓨터 입력 출력
    print("사용자 : " + human_act)
    print("컴퓨터 : " + com_act)

    # 결과 판정
    if human_act == com_act:
        result = "비김"
    elif human_act == "가위":
        if com_act == "보":
            result = "승리"
        else:
            result = "패배"
    elif human_act == "바위":
        if com_act == "가위":
            result = "승리"
        else:
            result == "패배"
    elif human_act == "보":
        if com_act == "바위":
            result = "승리"
        else:
            result = "패배"
    else:
        result = "입력오류"

    # 결과 출력
    if result == "승리":
        print("사용자가 승리하였습니다.")
        human_score = human_score + 1
    elif result == "패배":
        print("컴퓨터가 승리하였습니다.")
        com_score = com_score + 1
    elif result == "비김":
        print("비겼습니다.")
    else:
        result = "입력오류"
        print("가위 또는 바위 또는 보를 정확히 입력해주세요.")

    print(" ")
    print("현재 스코어, 사용자 : " + str(human_score) + ", 컴퓨터 : " + str(com_score))

    # 스코어 점검
    if human_score == 3:
        print("사용자의 최종 승리!")
        break
    elif com_score == 3:
        print("컴퓨터의 최종 승리!")
        break
    else:
        continue

    # 최종 판결 및 게임 종료
print("최종 스코어, 사용자 : " + str(human_score) + ", 컴퓨터 : " + str(com_score))
print("게임을 종료합니다.")
