import random

name = input("이름(영문): ")
age = int(input("나이: "))
price = int(input("상품 가격: "))
discount_rate = int(input("할인율(%): "))

# 1. 이름 처리: 소문자 변환 + 최대 5글자
processed_name = name.lower()[:5]

# 2. 나이 판별
grade = "성인" if age >= 20 else "미성년자"

# 3. 할인 가격 계산
discount_amount = price * discount_rate // 100
final_price = price - discount_amount

# 4. 로그인 ID 생성
random_number = random.randint(100, 999)
login_id = processed_name + str(random_number)

# 출력
print()
print(f"회원 등급: {grade}")
print(f"로그인 ID: {login_id}")
print(f"최종 결제 금액: {final_price}")