# age = int(input("Enter your age: "))
# if int(age) >=19 and age == "학생":
#     print("성인 학생")
# elif int(age) >=19 and age == "학생":
#     print("성인 비학생")
# else: 
#     print("미성년자")


age = int(input("나이를 입력하세요: "))
student = input("학생이면 '학생을 입력하세요.").strip()

if age >=19 and student == "학생":
    print("성인 학생")
elif age >=19:
    print("성인 비학생")
    
else:
    print("미성년자")

    '''[오답풀이]
    타입 혼동: age = int(...)로 나이를 정수로 바꿨는데 age == "학생"처럼 문자열과 비교하고 있습니다.
    조건 오류: elif의 조건이 if와 동일해서 두 번째 분기가 절대 실행되지 않습니다.
    불필요한 표현: else: 아래 int(age) <19처럼 표현은 아무 효과가 없습니다(조건문이 아님).
    '''