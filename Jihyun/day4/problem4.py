# age = int(input("나이를 입력하세요: "))
# student = input("학생 여부: ").strip()

# if  int(age) >= 19 and student == True:
#     print("성인 학생")
# elif int(age) >=19 and student != True:
#     print("성인 비학생")
# else:
#     print("미성년자")

age = int(input("나이를 입력하세요: "))
student = input("학생이면 학생, 비학생이면 비학생을 입력하세요: ").strip()

if age >=19 and student == "학생":
    print("성인 학생")
elif age >=19 and student != "학생":
    print("성인 비학생")
else:
    print("미성년자")

'''[오답풀이]
age = int(input("나이: "))
student_input = input("학생인가요? (yes/no): ")

if student_input == "yes":
    student = True
else:
    student = False

if age < 19:
    print("미성년자")
elif age >= 19 and student == True:
    print("성인 학생")
else:
    print("성인 비학생")
=====================================
stuent 변수를 문자열로 받았는데 불리언처럼 사용하려고 했다.
그래서 student 변수를 불리언으로 변환하는 과정이 필요한데, 
더 간결하게 작성하기 위해, student 변수를 문자열로 받은 후 바로 비교하도록 수정했다.
'''

# 또 다른 정답
age = int(input("나이를 입력하세요: "))

if age < 19:
    print("미성년자")
else:
    student = input("학생이면 '학생' 입력, 아니면 아무거나 입력: ").strip()
    if student == "학생":
        print("성인 학생")
    else:
        print("성인 비학생")
# 학생 입력을 나이 검사 이후로 옮기면 나이가 19 미만이면 바로 출력.