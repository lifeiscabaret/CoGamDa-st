name = input("영문 이름을 입력하세요: ")

user_id = ""
for i in range(len(name)):
    if i < 6:
        user_id += name[i].lower()

print(user_id)