try:
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print("결과:", result)
except:
    print("에러가 발생했습니다.")
except ValueError:
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")