#school class 만들기 실습

class School:
    def __init__(self, name, established, address):
        self.name = name
        self.established = established
        self.address = address

school1 = School("개발대학", "2017년 08월 07일", "이미지니어.io")
print(school1.name)
print(school1.established)
print(school1.address)
