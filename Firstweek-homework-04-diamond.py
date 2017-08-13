# 1주차 과제 4 - 다이아몬드 그리기

## 구현 내용
# 아래 도형을 구현
# 00100
# 01110
# 11111
# 01110
# 00100
# 5*5 좌표에 다이아몬드 그리기
# 반복문 (for-loop) 사용할 것

userInput = int(input("입력 :")) # 3
a = userInput # 3

for num in range(1,a+1): # 1, 2, 3
    print((a - num) * ' ' + ((2*num)-1) * '*')
for num in reversed(range(1,a)): # 2, 1
    print((a - num) * ' ' + ((2*num)-1) * '*')
