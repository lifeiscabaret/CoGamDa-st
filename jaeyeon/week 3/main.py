from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from pathlib import Path
from fastapi import HTTPException
from fastapi import Query

DB_PATH = Path("app.db")

app = FastAPI()

# FastAPI CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic 모델 정의 (Memo 클래스)
class Memo(BaseModel):
    title: str
    content: str


#
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


#
@app.get("/")
async def root():
    return {"msg": "This is root"}


#
@app.get("/ping")
def ping():
    return {"msg": "The place for ping test"}


#
@app.get("/memos")
def get_memos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM memo ORDER BY memo_id DESC")
    rows = cur.fetchall()
    memos = [dict(row) for row in rows]
    conn.close()
    return memos


#
@app.post("/memos")
def create_memo(memo: Memo):
    # title과 content는 memo 객체로 받음
    title = memo.title.strip()
    content = memo.content.strip()

    if not title:
        raise HTTPException(status_code=400, detail="TITLE REQUIRED")
    # if not content:
    #     raise HTTPException(status_code=400, detail="CONTENT REQUIRED")

    # 데이터베이스에 메모 추가
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO memo (title, content) VALUES (?, ?)", (title, content))
    conn.commit()

    memo_id = cur.lastrowid
    conn.close()

    return {"memo_id": memo_id, "title": title, "content": content}


#
@app.delete("/memos")
def delete_memo(id: int = Query(...)):  # id라는 이름의 쿼리 파라미터를 필수로 받음
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM memo WHERE memo_id = ?", (id,))
    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Memo not found")
    conn.close()
    return {"msg": "Memo deleted", "memo_id": id}
