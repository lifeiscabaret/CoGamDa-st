age = int(input('나이를 입력하세요:'))

if age<13:
    print('어린이')
elif age<19:
    print('청소년')
elif age>=19:
    print('성인')
else:
    print('나이가 부적절합니다.')