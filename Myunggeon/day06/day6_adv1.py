#로그인 ID 미니 버전

'''
사용자로부터 영문 이름을 입력받아
아래 조건에 맞는 ID를 생성하세요.
조건
이름을 소문자로 변환
앞에서 최대 6글자만 사용
for문 한 번 이상 사용
'''

ID = input("영문 이름을 입력하세요: ")
#소문자로 변환
lower_ID = ID.lower()

new_ID = ""

for i in range(6):
    #lower_ID의 각 항을 계속 더하기
    new_ID += lower_ID[i]
print(new_ID)


'''
<Claude AI의 문제풀이>
name = input("영문 이름을 입력하세요: ")

# 이름을 소문자로 변환
name_lower = name.lower()

# for문을 사용해서 앞에서 최대 6글자만 추출
user_id = ""
for i in range(len(name_lower)):
    if i < 6:
        user_id += name_lower[i]

print(f"생성된 ID: {user_id}")


<더 간단한 풀이>
name = input("영문 이름을 입력하세요: ")

user_id = ""
for char in name.lower()[:6]: #파이썬의 슬라이싱_범위를 지정하므로 길이가 6보다 짧으면 짧은대로 가져온다.
    user_id += char

print(f"생성된 ID: {user_id}")


<색다른 풀이>
name = input("영문 이름을 입력하세요: ")
lower_name = name.lower()

new_id = ""

for i in range(min(6, len(lower_name))):  # 이름 길이와 6 중 작은 값
    new_id += lower_name[i]

print(new_id)
'''


'''
<내 풀이의 문제점>
1.잠재적 에러 가능성

만약 사용자가 6글자보다 짧은 이름을 입력하면 IndexError가 발생합니다
예: "Tom" 입력 시 lower_ID[3]에서 에러


2.변수명

ID보다는 name이 더 의미가 명확할 것 같아요
Python 컨벤션상 변수명은 소문자와 언더스코어 사용을 권장합니다
'''