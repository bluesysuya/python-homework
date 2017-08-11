### 1주차 과제 2 - 회사 조직도 만들기

## 구현 내용
# 사람 클래스 생성, 기본 요소 : 이름, 나이, 성별
# 직장동료 클래스 생성, 추가 요소 : 직급

## 힌트
# 클래스, 상속 활용
# 사람의 기본 요소는 생성시 입력받을 것
# 직장 동료의 기본 직급은 "대리"
# (고급) 사람클래스에서 사람을 만들때 직급도 입력 받도록 한다.

class person:
    def __init__(self, name, age, gender, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = positions

class coworker(person):
    pass

print("신상정보를 입력합니다.")
name = input("이름 : ")
age = input("나이 : ")
gender = input("성별 : ")
position = input("직급 : ")

person1 = coworker(name, age, gender, position)
print(person1.name)
print(person1.age)
print(person1.gender)
print(person1.position)
