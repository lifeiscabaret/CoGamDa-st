# 반복 구조로 데이터 처리하기

'''
사용자로 부터 정수를 계속 입력받는다.
-while 문을 사용하자
입력한 값이 0이면 입력 종료
-break를 이용해 빠져 나오기
입력한 값이 음수이면 무시
-continue를 이용해서 무시
입력한 값이 양수이면 리스트에 저장
-append를 이용해서 리스트에 추가
리스트에 저장 된 값 중 짝수의 개수와 짝수의 합 출력
-x % 2 == 0 으로 짝수 판별
-짝수라면 for 문으로 count, sum 계산, sum() 함수 한 번 사용해보기
'''

numbers = int(input("정수를 입력하세요 (종료:0) : "))
even_list = [] # 짝수를 저장할 리스트
count_even = 0 # 짝수 개수

while True:
    if numbers == 0: # 0이면 입력 종료
        break
    elif numbers < 0: # 음수이면 무시
        numbers = int(input("정수를 입력하세요 (종료:0) : "))
        continue
    elif numbers % 2 != 0: # 홀수이면 무시
        numbers = int(input("정수를 입력하세요 (종료:0) : "))
        continue
    else: # 양수이면 리스트에 저장
        even_list.append(numbers)
        numbers = int(input("정수를 입력하세요 (종료:0) : "))
        count_even += 1

# 짝수의 합 계산
sum_even = 0
for i in range(len(even_list)):
    sum_even += even_list[i]

print("짝수의 개수 :", count_even)
print("짝수의 합 :", sum_even)