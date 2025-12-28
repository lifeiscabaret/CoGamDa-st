#중첩 조건 사고 연습

age = int(input("나이를 입력:"))
std = input("학생인가요? (y/n)으로 답변:")

'''
1.나이, 학생여부 입력
2.if 나이 확인, 중첩 if 학생여부 확인 - 들여쓰기0
3.나이 어리면 미성년자 출력 - 들여쓰기x
4.결과 출력
'''

if age >= 19:
    if std.lower() == "y":
        print("성인 학생")
    elif std.lower() =="n":
        print("성인 비학생")
else :
    print("미성년자")