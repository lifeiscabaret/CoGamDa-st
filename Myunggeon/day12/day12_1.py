# 루프 제어 구조 심화

'''
문제: "가장 느린 API 엔드포인트 찾기" (로그 수집기)
FastAPI 서버를 운영 중이라고 가정하고,
요청 로그를 콘솔에서 수집한다.
여러 API 요청의 경로(path)와 응답시간(ms) 를 입력받아,
가장 응답이 느렸던 API 경로를 출력하시오.
입력 예시:
반복해서 아래 2개 입력
1.API 경로 입력(예: /users, /login, /items/123)
2.응답시간(ms)입력 (정수)
단, API 경로에 STOP 을 입려하면 입력 종료한다.
(대소문자 모두 적용되게)
'''

'''
api경로와 시간의 변수 지정
리스트에 저장
while 문으로 반복
입력받은 문자 strip(), .lower()이용
빈문자열""이면 conitnue, stop입력되면 break
응답시간 입력받고 isdigit()으로 정수확인
정수 아니면 continue, 0미만도 continue
응답시간이 이전 응답시간보다 길다면 변수에 저장
변수가 바뀐게 없다면 NO LOGS 출력
'''

#변수 지정
path ="" 
time =0
logs =[]
#print(logs)

while True:
    path_sample = input("API경로 입력: ").lower().strip() #소문자 변환, 공백 제거
    #print(path_sample)
    if path_sample == "":
        print("EMPTY PATH")
        continue
    elif path_sample == "stop": #stop 입력했을때
        if not logs: #리스트가 비었다면
            print("NO LOGS")
        else:
            print(f"SLOWEST: {path} {time}ms")
        
        break #루프 탈출 반복문 종료

    else: #API경로가 정상일때만 응답시간 입력
        while True:
            time_sample = input("응답 시간: ")
            
            try: #int로 변환시도
                time_int = int(time_sample)

                #변환 성공 시
                if time_int <0:
                    print("NEGATIVE TIME")
                else: #0 이상의 정수이면
                    if time_int > time: #이전의 응답시간보다 느리다면
                        time = time_int #새로운 타임이 됨

                        path = path_sample #모든 조건 만족이므로 API주소도 등록
                        
                        logs.append([path,time])
                        break
                    else:
                        break #어떤 경우든 루프 탈출

            except: # 변환 실패시
                print("INVALID TIME")


                
