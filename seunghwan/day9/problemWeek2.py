# # 딕셔너리 이용해서 만들어 본것
while True:
    n = int(input("궁금하신 문의의 개수는 몇개이신가요?"))
    if 0<=n<=20:
        break
    else:
        print("잘못된 입력입니다.")

lst = []
label = {'PAYMENT':['pay', 'card', 'refund', 'price'],
         'ACCOUNT': ['login', 'password', 'signup', 'account'],
         'BUG': ['error', 'bug', 'crash', 'fail']}
CS = {'PAYMENT':[], 'ACCOUNT':[], 'BUG':[], 'OTHER':[]}

for _ in range(n):
    question = input("문의 내용을 영어로 적어주세요.")
    lst.append(question.strip().lower())

for i in range(n):
    play = False
    for category, keywords in label.items():                           #for label, keywords 하면 안됨 기존 label을 덮어버림
        if any([words in lst[i] for words in keywords]):               #근데 이건 words 대신에 keywords 해도 돌아감 왜지?     -> label.items()는 복사된것이지만 그 안에 label이 있는건 기존 변수를 덮음
            CS[category].append(lst[i])
            play = True
            break
    if play == False:
            CS['OTHER'].append(lst[i])

for key, value in CS.items():
    for rvalue in value:
        print(f"[{key}] {rvalue}")
print(f"PAYMENT:{len(CS['PAYMENT'])} ACCOUNT:{len(CS['ACCOUNT'])} BUG:{len(CS['BUG'])} OTHER:{len(CS['OTHER'])}")


# 딕셔너리 이용 안하고 배운것만 써서 만든것
lst = []
while True:
    n = int(input("궁금하신 문의의 개수는 몇개이신가요?"))
    if 0<=n<=20:
        break
    else:
        print("잘못된 입력입니다.")
        
for _ in range(n):
    question = input("문의 내용을 영어로 적어주세요.")
    lst.append(question.strip().lower())

Payment = ['pay', 'card', 'refund', 'price']
Account = ['login', 'password', 'signup', 'account']
Bug = ['error', 'bug', 'crash', 'fail']

Payment_sen = []
Account_sen = []
Bug_sen = []
Other_sen = []

for sentence in lst:
    for i in range(4):
        if Payment[i] in sentence:
            Payment_sen.append(sentence)
            break
        elif Account[i] in sentence:
            Account_sen.append(sentence)
            break
        elif Bug[i] in sentence:
            Bug_sen.append(sentence)
            break
    else:
        Other_sen.append(sentence)

for s in Payment_sen:
    print(f"[PAYMENT] {s}")
for s in Account_sen:
    print(f"[ACCOUNT] {s}")
for s in Bug_sen:
    print(f"[BUG] {s}")
for s in Other_sen:
    print(f"[OTHER] {s}")

print(
    f"PAYMENT:{len(Payment_sen)} "
    f"ACCOUNT:{len(Account_sen)} "
    f"BUG:{len(Bug_sen)} "
    f"OTHER:{len(Other_sen)}"
)