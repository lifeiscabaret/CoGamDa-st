from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #다른 도메인에서 오는 요청을 허용하기 위한 설정(리액트 앱이 이 서버와 통신하려면 필요)
import sqlite3 #간단 데이터베이스
from pydantic import BaseModel #데이터 검증을 위한 모델
from pathlib import Path #파일 위치 경로 네비게이션, 윈도우는 (\) 맥/리눅스는 (/)쓰는데 path쓰면 알아서 해준다.
from contextlib import asynccontextmanager #서버 셔터 여닫는 일 한다.

#데이터 베이스 파일 경로 설정
#현 폴더에 app.db가 여러개이므로 추가 작업
BASE_DIR = Path(__file__).parent # main.py가 현재 있는 폴더
DB_PATH = BASE_DIR/"app.db" #데이터베이스 파일 위치

app = FastAPI() #Fast API 앱 생성

#CORS 설정 - 보안 정책 우회하는 설정하기
#프론트엔드(HTML)와 백엔드(FastAPI)가 다른 포트에서 실행되므로 필요
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"], #모든 도메인에서의 요청 허용
    allow_credentials = True, #쿠키 포함 요청 허용
    allow_methods = ["*"], #모든 HTTP 메서드(GET, POST, DELETE 등) 허용
    allow_headers = ["*"] #모든 HTTP 헤더 허용
)

#데이터 베이스 초기화 함수
def init_db():
    """
    앱 시작 시 데이터베이스와 테이블을 생성하는 함수
    테이블이 이미 있으면 건너뛰고, 없으면 새로 만든다
    """
    conn = sqlite3.connect(str(DB_PATH)) # 테이터 베이스 연결
    cur = conn.cursor() # 커서 생성 (SQL 명령 실행)
    
    # 처음 한 번만 실행 후 주석 처리할 부분 - 존재하는 테이블 삭제
    #cur.execute("DROP TABLE IF EXISTS memo")
    
    # 새로 생성 (이미 있으면 건너 뜀...IF NOT EXISTS)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS memo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit() #변경사항 저장
    conn.close() #연결 종

# 시작 시 초기화 함수 실행
init_db()

#메모 생성용 데이터 모델 - 입력 데이터의 형식을 정의하고 검증 - 나중의 실수를 줄여줌
class MemoCreate(BaseModel):
    """
    POST 요청으로 메모를 생성할 때 받을 데이터 형식
    title과 content가 문자열(str)인지 자동으로 검증
    """
    title : str
    content : str

#데이터 베이스 연결 함수
def get_conn():
    """
    데이터베이스에 연결하고 Row 형식으로 데이터를 받도록 설정
    반환값: sqlite3 연결 객체
    """
    conn = sqlite3.connect(str(DB_PATH)) # DB 연결
    conn.row_factory = sqlite3.Row #row_factory는 데이터를 딕셔너리 처럼 쓸 수 있게 해준다 (row['title'])
    return conn

#기본 엔드포인트 - 서버가 정상 작동하는 지 확인용
@app.get("/") # 루트 경로로 GET요청이 오면 실행
async def root():
    """
    서버 상태 확인용 엔드포인트
    브라우저에서 http://127.0.0.1:8000/ 접속하면 {"msg":"hello world"} 반환
    """
    return {"msg":"hello world"}

#모든 메모 조회
#데이터 베이스에서 메모를 가져와서 JSON 형태로 리턴
@app.get("/memos") #memos는 URL 꼬리표, /memos 경로로 GET 요청이 오면 실행
def get_memos():
    conn = get_conn() #conn - 고속도로
    cur = conn.cursor() #cursor - 짐꾼
    cur.execute("SELECT*FROM memo ORDER BY created_at DESC") #최신 순 정렬
    rows = cur.fetchall() #조회 된 모든 행 가져오기
    memo = [dict(row)for row in rows] #각 행을 딕셔너리로 변환하여 리스트에 담기
    conn.close()
    return memo # JSON 형태로 반환 (fastAPI가 자동변환)

#메모 생성 엔드포인트 
@app.post("/memos") # /memos 경로로 POST 요청이 오면 실
def create_memo(memo: MemoCreate):
    """
    새로운 메모를 데이터베이스에 저장
    입력: MemoCreate 모델 (title, content)
    반환: 생성된 메모 정보 (id, title, content)
    """
    conn = get_conn() # 데이터베이스 연결
    cur = conn.cursor() # 커서 생성

    #SQL 쿼리 실행: memo 테이블에 새 데이터 삽입
    #?는 플레이스홀더 - SQL Injection 공격 방지
    cur.execute(
        "INSERT INTO memo (title, content) VALUES(?, ?)",
        (memo.title, memo.content) #title과 content 둘 다 안전하게 저장
    )

    conn.commit() #변경사항 저장
    memo_id = cur.lastrowid #lastrowid: 방금 추가된 데이터의 ID 가져오기
    conn.close() #연결 종료

    # 생성된 메모 정보 반환
    return{
        "id": memo_id,
        "title": memo.title,
        "content": memo.content
    }
