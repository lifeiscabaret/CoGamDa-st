#continue + 조건 조합

nums = (1,2,3,4,5,6,7,8,9,10)

#continue는 아래 코드를 건너뛰고 다음 반복으로 넘어가게 한다.
#for 반복문 사용
for n in nums:
    if n% 2 ==0:
        continue
    print(n)

#while 반복문 사용
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        i += 1
        continue
    print(nums[i])
    i += 1