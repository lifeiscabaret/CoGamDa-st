#응용문제. 조건 + 누적

nums = [1,2,3,4,5,6]

#짝수의 합만 구해서 출력하기.
sum = 0
for i in nums:
    if i % 2 ==0:
        sum += i
        #print(sum)
print(sum)