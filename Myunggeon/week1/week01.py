#간단한 회원 정보 처리 프로그램

name = input("이름을 영어로 입력: ")
age = int(input("나이를 입력: "))
price = int(input("상품 가격 입력: "))
discount_rate = int(input("할인율(%): "))

#회원 등급 출력
if age >= 20:
    print("회원 등급 : 성인")
else:
    print("회원 등급 : 미성년자")

#로그인 ID 출력
#소문자 변환 name.lower()[] 혹은 name[].lower()로도 표현 가능
change_name = name.lower()[0:5]

#random 모듈 불러오기
import random
#random.randint(a,b) = 랜덤한 정수
#random.randrange(a,b) = 끝값을 미포함한 랜덤한 정수
#random.randrange(a,b,c) = c 단위로 뛰어넘는 랜덤한 정수, b 미포함
ran_num = random.randint(100,999)

#f-string 문자열 포맷 방식 (f"{변수}")
#문자열 내에 변수나 표현식을 직접 삽입할 수 있는 방식
print(f"로그인 ID: {change_name}{ran_num}")

#최종 결제 금액 출력
discount_price = price * (discount_rate/100)
final_price = price - discount_price
print("최종 결제 금액: ",final_price)