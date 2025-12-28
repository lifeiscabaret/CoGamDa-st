#중첩 if → elif 변환 감각

age = int(input("나이 입력:"))
std = input("학생입니까? (T/F)로 입력:")

if age < 19 :
    print("미성년자")

# 어차피 age가 19보다 작은 경우라서 age >=19필요 없음.
elif std =="T":
    print("성인 학생")
else :
    print("성인 비학생")