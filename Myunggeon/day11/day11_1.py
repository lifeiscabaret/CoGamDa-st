# 루프 제어 구조
'''
하루 방문자 수 중 최댓값 찾기
어떤 서비서의 하루 방문자 수를 여러번 입력받아,
가장 많이 방문한 날의 방문자 수(최댓값)를 출력하시오
'''

'''
5번 입력받는다는 전제조건이 있기 때문에
while 문을 사용하여 방문자 수를 입력받는다.
만약 음수인 값이 입력되면 "INALID"를 출력하고
continue 문을 사용하여 다시 루프를 돌리고
count 변수를 1 증가시키지 않는다.
정수가 제대로 입력 됐다면
count 변수를 1 증가시키고 변수에 저장한다.
다음 루프에서 변수와 입력받은 값을 비교하여
입력받은 값이 더 큰 값을 변수에 저장한다.
최종적으로 변수에 저장된 값을 출력한다.
'''

max_visitors = 0  # 최댓값을 저장할 변수
count = 0  # 입력 횟수를 세기 위한 변수

while count < 5:
    visitors = int(input("하루 방문자 수를 입력하세요: "))
    
    if visitors < 0:
        print("INVALID")
        continue  # 음수인 경우 루프의 처음으로 돌아감
    
    count += 1  # 유효한 입력이 들어왔으므로 카운트 증가
    
    if visitors > max_visitors:
        max_visitors = visitors  # 최댓값 갱신

print(count, "번의 유효한 입력이 처리되었습니다.")
print("가장 많이 방문한 날의 방문자 수:", max_visitors)