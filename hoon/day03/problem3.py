#문제
'''
문자열을 입력받아
문자 "a"가 포함되어 있으면 "a 있음"
포함되어 있지 않으면 "a 없음"을 출력하시오.
'''

#풀이
words = input("문자열을 입력하세요: ")
if words.find("a") != -1:
    print("a 있음")
else:
    print("a 없음")

# 어려운 부분
# day02/problem4.py의 find() 활용과 헷갈림
# != -1 조건 활용 힌트 보고 if문 수정