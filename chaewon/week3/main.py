# Week3

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # FastAPI의 응답 도구들 중 파일을 전송하기 위한 전용 도구(FileResponse)를 가져온다.
import sqlite3
from pathlib import Path
from contextlib import asynccontextmanager

# 1. DB 파일 경로 설정
DB_PATH = Path("app.db")

# 2. 데이터베이스 및 테이블 초기화 함수
def init_db():
    # 데이터베이스 파일에 연결(없으면 새로 만든다.)
    conn = sqlite3.connect(DB_PATH)
    # SQL 명령어를 실행하기 위한 커서(일꾼)를 만드는 것.
    cur = conn.cursor()
    # 테이블명 memo, 컬럼명 memo_id, title, content (과제 내용 중 2)메모추가 - 응답 형태 예시를 따름.)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS memo (
            memo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 3. 서버 실행 시 DB 초기화(lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

# 왼쪽의 lifespan= 은  FastAPI라는 프로그램이 미리 정해둔 '칸 이름'.
# 왼쪽의 lifespan= 은 여기에 서버 시작/종료 시 실행할 로직을 넣어줘라 라고 만들어둔 일종의 서류 양식 칸.
# 오른쪽의 lifespan은 위에서 직접 만든 함수의 이름.
# 그냥 FastAPI(lifespan)이라고 쓰면 안 됨.
# lifespan= 을 생략하면 컴퓨터는 순서대로 데이터를 파악한다.
# 하지만 FastAPI() 안에는 제목(title), 설명(description), 버전(version) 등 수십 개의 칸이 있다.
# lifespan= 을 붙여야 컴퓨터가 어느 칸에 넣을지 정확히 알아먹는다.
app = FastAPI(lifespan=lifespan)

# 4. CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. DB 연결 함수
# def get_db() = 필요할 때마다 DB에 연결해서 데이터를 꺼내올 준비를 하는 함수
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 6. 홈 화면 접속 시 index.html 보여주도록
# @app.get("/") = "사용자가 홈페이지 주소로 들어오자마자 실행해라"
@app.get("/")
# def read_index = "인덱스(첫 화면)을 읽어라"라는 뜻으로 지은 이름
async def read_index():
    # return FileResponse("index.html") = "미리 준비한 'index.html' 파일을 사용자 브라우저에 전달하라"
    # FileResponse = FastAPI가 제공하는 특수 기능.
    # FileResponse = 단순한 텍스트가 아니라 '실제 파일'을 통째로 응답(Response)으로 보내줄 때 사용
    return FileResponse("index.html")

# [요구사항 1] 메모 목록 조회
@app.get("/memos")
def get_memos():
    # 위에서 만든 get_db 함수를 호출해 conn(=Connection)변수에 저장
    conn = get_db()
    cur = conn.cursor()
    # 최신순(memo_id DESC)으로 반환
    cur.execute("SELECT * FROM memo ORDER BY memo_id DESC")
    rows = cur.fetchall()
    memos = [dict(row) for row in rows]
    conn.close()
    return memos

# [요구사항 2] 메모 추가
@app.post("/memos")
def create_memo(
    title: str = Query(...), # 사용자로부터 제목을 필수로 받는다. (필수 입력)
    content: str = Query("") # 내용은 없으면 빈 문자열("")로 처리한다. (선택 입력, 기본값 빈 문자열)
):
    # title이 비어 있거나 공백만 있는지 확인한다
    if not title or title.strip() == "":
        # 비어 있다면 400 에러(잘못된 요청)와 함께 메시지를 보낸다.
        raise HTTPException(status_code=400, detail="TITLE REQUIRED")

    conn = get_db()
    cur = conn.cursor()
    # 제목과 내용을 테이블에 삽입(INSERT)한다. ?는 보안을 위한 빈칸이다.
    cur.execute("INSERT INTO memo (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    
    # 방금 저장된 데이터의 ID(번호)를 가져온다.
    new_id = cur.lastrowid
    conn.close()
    
    return {"memo_id": new_id, "title": title, "content": content}