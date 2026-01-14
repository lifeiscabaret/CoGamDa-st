from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #다른 도메인에서 오는 요청을 허용하기 위한 설정(리액트 앱이 이 서버와 통신하려면 필요)
import sqlite3 #간단 데이터베이스
from pathlib import Path #파일 위치 경로 네비게이션, 윈도우는 (\) 맥/리눅스는 (/)쓰는데 path쓰면 알아서 해준다.
from contextlib import asynccontextmanager #서버셔터 여닫는 일 한다.

DB_PATH = Path("app.db") #데이터베이스 파일 위치
app = FastAPI() #Fast API 앱 생성

#CORS 설정 - 보안 정책 위회하는 설정하기
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#리뷰 생성용 데이터 모델 - 실수를 덜어줌
class MemoCreate(BaseModel):
    title : str
    content : str

#데이터 베이스 연결 함수
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row #row_factory는 데이터를 딕셔너리 처럼 쓸 수 있게 해준다
    return conn

#기본 엔드포인트 - 서버가 정상 작동하는 지 확인용
@app.get("/") # 루트 경로로 GET요청이 오면 실행
async def root():
    return {"msg":"hello world"}

#모든 메모 조회
#데이터 베이스에서 메모를 가져와서 JSON 형태로 리턴
@app.get("/memos") #memos는 URL 꼬리표, 리액트에서 fetch('/memos')로 호출하면 목록을 받을 수 있다.
def get_memos():
    conn = get_conn() #conn - 고속도로
    cur = conn.cursor() #cur - 짐꾼
    cur.execute("SELECT*FROM memo ORDER BY created_at DESC") #최신 순 정렬
    rows = cur.fetchall()
    memo = [dict(row)for row in rows]
    conn.close()
    return memo

#메모 생성
@app.post("/memos")
def create_memo(memo: MemoCreate):
    conn = get_conn()
    cur = conn.cursor()
    #title과 content 둘 다 저장
    cur.execute(
        "INSERT INTO memo (title, content) VALUES(?, ?)",
        (memo.title, memo.content)
    )
    conn.commit()
    memo_id = cur.lastrowid #lastrowid: 방금 추가된 데이터의 ID
    conn.close()

    return{
        "id": memo_id,
        "title": memo.title,
        "content": memo.content
    }
