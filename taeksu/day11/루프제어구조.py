# 1차 시도
# customers_per_day = int(input("하루 방문자 수:"))
# customers = []

# while True:
#     for day in range(0, 6):
#         if customers_per_day < 0:
#             print("INVALID")
#             break
#         else:
#             continue
            
#     print(max(customers))

# 2차 시도
# customers = []

# while True:
#     for i in range(0, 5):
#         int(input("하루 방문자 수"))
#         i += 1
#         customers = i
#         if i < 0:
#             print("INVALID")
#             continue
        
#     best_of_the_day = max(customers)
#     print(best_of_the_day)

# 3차 시도
# customers = []

# while True:
#     for i in range(0, 5):
#         int(input("하루 방문자 수:"))
#         if i >= 0:
#             customers.append(i)
#         else:
#             print("INVALID")
#     continue

#     print(max(customers))
    
# 4차 시도
# customers = []

# for i in range(0, 5):
#     customers_of_the_day = int(input("하루 방문자 수:"))
#     if i >= 0:
#         customers.append(customers_of_the_day)
#     else:
#         print("INVALID")

#     print(max(customers))

# 5차 시도
# customers = []
# days = ["월", "화", "수", "목", "금"]

# for i in range(0, 5):
#     for j in days:
#         customers_of_the_day = int(input(f"{j}요일 방문자 수:"))
#         if customers_of_the_day >= 0:
#             customers =+ 1
#         else:
#             print("INVALID")
#             continue
#         customers =- 1        

# the_best_of_the_day = max([customers])
# print(f"가장 많이 방문한 날의 방문자 수(최댓값): {days} {the_best_of_the_day}")

# 6차 시도
# customers = []
# days = ["월", "화", "수", "목", "금"]

# for idx, day in enumerate(days):
#     customers_of_the_day = int(input(f"{day}요일 방문자 수:"))
#     if customers_of_the_day >= 0:
#         idx += 1
#         the_best_of_the_day = max([customers])
#     else:
#         print("INVALID")
#         continue
#     customers =- 1
        
#     print(f"가장 많이 방만한 날의 방문자 수(최댓값): {day}요일 {the_best_of_the_day}")
    
# 7차 시도
# customers = []  
# max_customers = 0

# for day in ["월", "화", "수", "목", "금"]:
#     while True:
#         the_customers_of_the_day = int(input(f"{day}요일 하루 방문자 수:"))
#         if the_customers_of_the_day >= 0:
#             customers += [the_customers_of_the_day]
#             break
#         if customers > [the_customers_of_the_day]:
#             max(customers)
#         else:
#             print("INVALID")
#             continue
        
#     print(f"가장 많이 방만한 날의 방문자 수(최댓값): {day}요일 {customers}")

# 8차 시도
max_customers = 0

for day in ["월", "화", "수", "목", "금"]:
    while True:
        the_customers_of_the_day = int(input(f"{day}요일 하루 방문자 수:"))
        
        if the_customers_of_the_day >= 0:
            if the_customers_of_the_day > max_customers:
                max_customers = the_customers_of_the_day
                
            break
        
        else:
            print("INVALID")
            continue
        
print(f"가장 많이 방문한 날의 방문자 수(최댓값): {max_customers}")