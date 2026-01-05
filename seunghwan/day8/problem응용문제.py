# if-else 이용
while True:
    number = int(input('숫자를 입력하시오:'))
    if number == 0:
        print('종료')
        break
    else:
        print(f'입력한 숫자는 {number}입니다.')

# continue 이용
while True:
    number = int(input('숫자를 입력하시오:'))
    if number != 0:
        print(f'입력한 숫자는 {number}입니다.')
        continue

    print('종료')
    break    