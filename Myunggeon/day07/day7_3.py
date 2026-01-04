#실전문제. 

'''
문제
사용자로부터 영문 문자열 하나를 입력받아
아래 조건에 맞게 처리하는 프로그램을 작성하시오.
처리 조건
1️⃣ 문자열을 소문자로 변환한다
2️⃣ 문자열을 한 글자씩 반복하면서
3️⃣ 모음(a, e, i, o, u)의 개수를 센다
'''

words = input("영문 문자열을 입력하세요: ")
vowels = ["a","e","i","o","u"]
nums = 0
#소문자로 변환
words_lower = words.lower()
for i in words_lower:
        for j in vowels:
            if i == j:
                nums += 1
print(nums)

'''
<코드 리뷰_Claude>
👍 잘한 점:

문제의 모든 조건을 정확히 만족했습니다
이중 for문을 사용해서 논리적으로 올바르게 구현했습니다
변수명이 의미가 명확합니다

💡 개선 가능한 점:

1.효율성 측면

현재는 각 문자마다 모음 리스트 5개를 모두 확인합니다 (O(n×5))
in 연산자를 사용하면 더 간결하고 읽기 쉽습니다


2.변수명

nums보다는 vowel_count 같은 이름이 더 명확할 것 같아요


<리팩토링>
name = input("영문 문자열을 입력하세요: ")
vowels = "aeiou"  # 리스트 대신 문자열로 써도 'in'으로 비교 가능합니다
count = 0

# 1. 소문자로 변환된 문자열을 한 글자씩 반복
for char in name.lower():
    # 2. 현재 글자가 모음 묶음(vowels)에 포함되어 있는지 확인
    if char in vowels:
        count += 1

print(f"모음의 개수: {count}")


<in 연산자>
1. in 연산자의 기본 원리
in 연산자는 왼쪽의 값이 오른쪽의 데이터 집합에 포함되어 있으면 True, 없으면 False를 돌려줍니다.

2. 다양한 데이터 타입에서의 활용
in은 문자열뿐만 아니라 파이썬의 모든 '묶음 자료형(Iterable)'에서 사용할 수 있습니다.

●리스트[List] / 튜플(Tuple)_불변성이 있는 묶음: 특정 요소가 있는지 확인
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True

●딕셔너리(Dictionary): 특정 **키(Key)**가 존재하는지 확인
user = {"name": "Alice", "age": 25}
print("name" in user)  # True (키를 찾음)
print("Alice" in user) # False (값은 기본적으로 찾지 않음)

●문자열(String): 부분 문자열(Substring)이 포함되었는지 확인
print("py" in "python") # True

3. 반대되는 연산자: not in
"안 들어있으면 실행해라"라는 로직을 짤 때는 not in을 사용합니다. 코드가 훨씬 직관적인 영어 문장처럼 보이죠.
banned_users = ["bad_guy", "spammer"]
user = "good_student"

if user not in banned_users:
    print("입장 가능합니다.")
'''