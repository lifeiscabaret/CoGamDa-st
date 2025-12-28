#문제
'''
문자열을 입력받아
문자 "a"가 처음 등장하는 위치를 출력하시오.
'''

#풀이
words = input("문자열을 입력해주세요: ")
a_position = words.find("a")
#-1 출력 확인 후 if문 응용 출력
if a_position == -1:
    print("문자 a가 없습니다.")
else:
    print("문자 a의 위치는", a_position, "입니다.")