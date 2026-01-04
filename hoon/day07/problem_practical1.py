a = input("문자열을 입력하세요: ").lower()

vowels = ["a", "e", "i", "o", "u"]
count = 0

for ch in a:
    if ch in vowels:
        count += 1

print("모음 개수:", count)

#추가 코드 strip()
'''
a = input("문자열을 입력하세요: ").strip().lower()
공백 제거
'''