#반올림 점수 판별
num = float(input("실수 하나 입력:"))

#round() : 숫자를 반올림 해주는 함수
#round(숫자, 자릿수) 로 사용. 자릿수 없으면 정수로 반환
if round(num) >= 90:
    print("합격")
else:
    print("불합격")