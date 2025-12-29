#문제
'''
사용자의 나이(age)와 학생 여부(student)를 입력받아 출력하시오.
미성년자 → “미성년자”
성인 학생 → “성인 학생”
성인 비학생 → “성인 비학생”
'''

#풀이
age = int(input("나이를 입력하세요: "))
student = input("학생인가요? ")

if age < 19:
    print("미성년자")
elif student == "True":
    print("성인 학생")
else:
    print("성인 비학생")


#추가하면 좋을 사항: 배웠던 upper() 사용하여 학생 여부 입력을 대소문자 구분 없이 "TRUE"로 처리
'''
age = int(input("나이를 입력하세요: "))
student = input("학생인가요? ").upper() 

if age < 19:
    print("미성년자")
elif student == "TRUE":
    print("성인 학생")
else:
    print("성인 비학생")
'''