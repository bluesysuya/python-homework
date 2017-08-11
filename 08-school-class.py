#school class 만들기 실습

class School:
    def __init__(self, name, established, address):
        self.name = name
        self.established = established
        self.address = address

print("학교 정보를 입력하세요.")
print(" ")

name = input("학교이름 : ")
established = input("설립년도 : ")
address = input("주소 : ")

print(" ")
print("입력한 정보는 다음과 같습니다.")
school1 = School(name, established, address)
print("학교이름 : " + school1.name)
print("설립년도 : " + school1.established)
print("주소 : " + school1.address)
