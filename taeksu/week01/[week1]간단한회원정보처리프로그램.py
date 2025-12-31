a = input("이름을 입력하시요: ")
a = a.lower()

b = int(input("나이를 입력하세요: "))
if b >= 20:
    print(f"{a} 님은 성인니다.")
else:
    print(f"{a} 님은 미성년자입니다.")

price = int(input("가격을 입력해주세요: "))
discount_rate = 0.1 # 10% 할인율
discount_price = price * discount_rate
final_price = price - discount_price
print(f"최종 결제 금액은 {final_price}원 입니다.")