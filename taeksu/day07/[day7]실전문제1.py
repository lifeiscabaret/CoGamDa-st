ch = input("영문 문자열 하나를 입력하시오:")
ch = ch.lower()
vowels = ["a", "e", "i", "o", "u"]
total = 0

for character in ch:
    if character in vowels:
        total += 1

print(total)