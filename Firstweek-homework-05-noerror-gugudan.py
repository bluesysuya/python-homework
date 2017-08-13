# 1주차 과제 5 - 에러 나지 않는 구구단

# 숫자 입력받아 구구단 출력하기 (2~9단)
# 2~9를 제외한 다른 수를 입력받을 경우
# "2에서 9사이의 숫자만 입력해주세요." 문구 출력후 입력과정 재실행

# 에러처리 사용할 것

class InputError(Exception):
    pass

def ggd():
    try:
        dan = int(input("몇 단을 출력 하시겠습니까? : "))
        if dan > 1 and dan < 10:
            for num in range(1,10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            raise InputError()
    except InputError:
        print(" ")
        print("2에서 9사이의 숫자만 입력해주세요.")
        print(" ")
        ggd()

ggd()
