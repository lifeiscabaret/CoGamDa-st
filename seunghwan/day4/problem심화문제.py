number = int(input('정수를 입력하세요:'))

if number%3 == 0 and number%2 ==0:
    print('6의 배수')
elif number%3 == 0:
    print('3의 배수')
elif number%2 == 0:
    print('2의 배수')
else:
    print('해당 없음')