letter = input('영문 이름을 입력하세요:')

letter = letter.lower()
new_letter = ''

for i in range(6):
    new_letter += letter[i]

print(new_letter)