age = int(input('나이를 입력하세요:'))
studentYes = input('학생 여부를 입력하세요(학생이면 True, 아닐 경우 False):') == 'True'


if age>=19 and studentYes:
    print('성인 학생')
elif age>=19 and not studentYes:
    print('성인 비학생')
elif age<19 and studentYes:
    print('미성년자 학생')
elif age<19 and not studentYes:
    print('미성년자 비학생')
else:
    print('부적절한 입력')