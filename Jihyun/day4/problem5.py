a = int(input("정수를 입력하세요:"))

if (a%2 == 0) and (a%3 ==0) ==True:
    print("6의 배수")
elif a%2 == 0:
    print("2의 배수")
elif a%3 == 0:
    print("3의 배수")
else:
    print("해당없음")

#====오답풀이=====#
# if (a%2 == 0) and (a%3 ==0) ==True: 
# if a%2 and a%3 ==0 
# 가로와 True 생략으로 
# ❌ "2의 배수"를 정확히 검사하지 못함