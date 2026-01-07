#break/continue 실전 적용

for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i,j)


'''
continue는 바로 아랫줄을 건너뛰는 명령어이기 때문에
j = 1 이 True라면 Print를 건너뛴다.
건너뛴 후에 다시 반복문이 시작된 
for i in range(3):으로 넘어가서
i 변수 내에 존재하는 다음 값으로 넘어가 계산을 계속한다.
따라서 출력 결과는
0 0
0 2
1 0
1 2
2 0
2 2
'''
