#조건 흐름 파악

age = int(input("나이 입력:"))

if age >=0 and age < 13:
    print("어린이")
elif age <19 and age >= 13:
    print("청소년")
elif age >= 19:
    print("성인")
else :
    print("올바른 값 아님")