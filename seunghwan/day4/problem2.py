age = int(input('나이를 입력하세요:'))
studentYes = input('학생 여부를 입력하세요. 학생일 경우 "학생", 학생이 아닌 경우 "비학생"으로 입력하세요')

if age>=19:
    if studentYes=='학생':
        print('성인 학생')
    elif studentYes=='비학생':
        print('성인 비학생')
    else:
        print('부적절한 입력')
else:
    if studentYes=='학생':
        print('미성년자 학생')
    elif studentYes=='비학생':
        print('미성년자 비학생')
    else:
        print('부적절한 입력')