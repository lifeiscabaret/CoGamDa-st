nums = [1, 2, 3, 4, 5, 6]
total = 0

for n in nums:
    if n % 2 == 0:
        total += n

print("짝수 합:", total)