# a = int(input("나이를 입력하시오: "))
# a = abs(a)

# if a < 19:
#     print("미성년자")
# elif a >= 19:
#     stu = input("학생인가요: ")
#     if a >= 19 and stu == True:
#         print("성인 학생")
#     else:
#         print("성인 비학생")

a = int(input("나이를 입력하시오: "))
age = abs(a)

if age < 19:
    print("미성년자")
elif age >= 19:    
    stu = input("학생인가요: ")
    if stu == "True":
        print("성인 학생")
    else:
        print("성인 비학생")