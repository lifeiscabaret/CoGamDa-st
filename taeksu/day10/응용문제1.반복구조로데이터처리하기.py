# num = int(input("정수를 입력하세요:"))
# count = []

# while num == 0:
#     break
# for i in range(-num):
#     continue
# if num >= 1:
#     count += [1]
    
# if len(count) % 2 == 0:
#     print(f'짝수의 개수: {} "," 짝수의 합: {}') 

# num = int(input("정수를 입력하세요:"))

# while True:
#     if num == 0:
#         break
#     elif num < 0:
#         continue
#     else:
#         even_len = 0
#         even_sum = 0
        
#     for i in range(1, num+1):
#         if i % 2 == 0: # 짝수인지 확인
#             even_len += 1
#             even_sum += i
            
#     print(f"짝수의 개수: {even_len}, 짝수의 합: {even_sum}")

while True:
    num = int(input("정수를 입력하세요:"))
    
    if num == 0:
        print("종료")
        break # 0을 입력하면 반복문 종료
    
    elif num < 0:
        continue # 다시 루프의 처음(입력 단계)으로 돌아감
    
    # 계산 로직
    even_len = 0
    even_sum = 0
    
    for i in range(1, num + 1):
        if i % 2 == 0:
            even_len += 1
            even_sum += i
            
    print(f"짝수의 갯수는: {even_len}, 짝수의 합은: {even_sum}")