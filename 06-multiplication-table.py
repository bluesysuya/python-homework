# 숫자 입력받아 구구단 출력하기 (2~9단)

print("구구단 출력 프로그램")
print(" ")

# 숫자 입력
n = input("몇 단을 출력하시겠습니까? ")

# 입력된 숫자가 2~9가 아닐 경우
if int(n) < 2 or int(n) > 9:
    print("2~9단만 출력가능합니다.")

# 입력된 숫자가 2~9일 경우 해당 구구단 출력
# for
if int(n) >= 2 and int(n) <= 9:
    print(n + "단을 출력합니다. (for 사용)")
    for num in range(1,10):
        result = int(n) * num
        # print(n)
        # print(num)
        # print(result)
        print(n + " * " + str(num) + " = " + str(result))

# while
if int(n) >= 2 and int(n) <= 9:
    print(n + "단을 출력합니다. (while 사용)")
    num = 1
    while num < 10:
        result = int(n) * num
        print(n + " * " + str(num) + " = " + str(result))
        num = num + 1


# # 답안
# # 1) 사용자로부터 몇 단을 출력할 지 받을 것
# # 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것
#
# dan = int(input("몇 단을 출력 하시겠습니까?"))
# # 원래 답안
# for num in range(1, 10):
#     print("{} * {} = {}".format(dan, num, dan * num))
#
# # 원래 1~9단까지만 실행하고 싶다면?
# # if dan > 0 and dan < 10:
# #     for num in range(1, 10):
# #         print("{} * {} = {}".format(dan, num, dan * num))
# #     else:
# #         print("1에서 9사이의 숫자를 넣어주세요.")


# Self Feedback
# int(input())으로 문자가 아닌 정수값으로 바로 입력받을 수 있다.
# format을 사용하면 더 간편
