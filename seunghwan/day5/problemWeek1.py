import random

name_processed = ''
age_processed = 0
price_processed = 0

name = input('영문 이름을 입력하세요:')
age = int(input('나이를 입력하세요:'))
price = int(input('상품 가격을 입력하세요:'))
discount = int(input('할인율(%)을 입력하세요:'))

name_processed = name.lower()[:5]
age_processed = '성인' if age >=20 else '미성년자'                         ## 삼항 연산자 사용
price_processed = (lambda p, d: p * (100 - d) / 100)(price, discount)    ## 람다 함수 사용
random_ID = random.randint(100,999)

print(f'회원등급 : {age_processed}')
print(f'로그인 ID : {random_ID}')
print(f'최종 결제 금액 : {price_processed}')