# for문만 이용
for i in range(1, 11):
    if i >= 7:
        break
    if i % 2 != 0:
        print(i)


# while + if문 이용
i = 1
while i < 11:
    if i >= 7:
        break
    if i % 2 != 0:
        print(i)
        i += 1
        continue
    else:
      i += 1