name = input("영어 이름을 입력하세요:")

total = 0

for char in name.lower():
    if char in 'aeiou':
        total += 1
print(total)