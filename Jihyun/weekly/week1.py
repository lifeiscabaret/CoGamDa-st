import random 

name = input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:" ))
price = int(input("상품 가격:"))
discount = int(input("할인율 % :"))

a = name.lower()[0:5]

if age >=20:
    # print("성인")
    grade = "성인"
else:
    # print("미성년자")
    grade = "성인"
discount_price = price * discount / 100
final_price = price - discount_price

random_number = random.randint(1,100)
login_id = a + str(random_number)

print("회원 등급:", grade)
print("로그인 ID:", login_id)
print("최종 결제 금액:", final_price)