import random

# 입력
name = input("이름 영문: ")
age = int(input("나이: "))
price = int(input("상품 가격: "))
discount_rate = int(input("할인율(%): "))

# 처리
# 1 - 이름 처리
processed_name = name.lower()[0:5]

# 2 - 나이 판별
if age >= 20:
    grade = "성인"
else:
    grade = "미성년자"

# 3 - 할인 가격 계산
discount_amount = price * (discount_rate / 100) # 할인받는 금액
final_price = price - discount_amount           # 최종 가격

# 4 - 로그인 ID 생성
random_num = random.randint(100, 999)
login_id = f"{processed_name}{random_num}"

# 출력
print(f"회원 등급: {grade}")
print(f"로그인 ID: {login_id}")
print(f"최종 결제 금액: {int(final_price)}")