# 중첩 조건 사고 연습
# age = int(input("나이를 입력하시오: "))
# age = abs(age)
# stu = input("학생인가요: ")

# if age > 19 and stu != -1: # 왜 and 를 사용하면 안되지?
#     print("성인 학생")
# elif age >= 19 and stu == -1:
#     print("성인 비학생")
# else:
#     print("미성년자")

# age = int(input("나이를 입력하시오: ")) 
# age = abs(age)
# stu = input("학생인가요: ")

# if age >= 19:
#     if stu == "예":
#         print("성인학생")
#     else :
#         print("성인 비학생")
# if age < 19:
#     print("미성년자") # 왜 학생여부를 묻는 거지?

age = int(input("나이를 입력하시오: "))
age = abs(age)

if age >= 19:
    stu = input("학생인가요: ")
    if stu == "예":
        print("성인 학생")
    else:
        print("성인 비학생")
else:
    print("미성년자")