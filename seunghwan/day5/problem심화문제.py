number = int(input('숫자를 입력하세요:'))

message = ''                            ## 빈 문자열로 초기화

if abs(number) > 5:
    message = '범위 초과'
else:
    message = '정상 범위'

print(message)