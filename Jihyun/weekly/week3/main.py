from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pathlib import Path

DB_PATH = Path("app.db")

app = FastAPI()

# 프론트(React)에서 API 호출 가능하도록 CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "ok"}

# 메모 목록 조회: DB의 메모를 최신순으로 반환
@app.get("/memos")
def get_memos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT memo_id, title, content FROM memo ORDER BY memo_id DESC")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# 메모 단건 조회: memo_id로 특정 메모를 1개 반환
@app.get("/memos/{memo_id}")
def get_memo(memo_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT memo_id, title, content FROM memo WHERE memo_id = ?", (memo_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="NOT FOUND")
    return dict(row)

# 메모 추가: Query Parameter로 입력받아 DB에 저장 후 저장된 데이터를 반환
@app.post("/memos")
def create_memo(title: str, content: str = ""):
    if title is None or title.strip() == "":
        raise HTTPException(status_code=400, detail="TITLE REQUIRED")
    title = title.strip()
    content = "" if content is None else content

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO memo (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    memo_id = cur.lastrowid
    conn.close()

    return {"memo_id": memo_id, "title": title, "content": content}

# 메모 수정: memo_id의 title/content를 부분 수정(PATCH)하고 수정된 데이터를 반환
@app.patch("/memos/{memo_id}")
def update_memo(memo_id: int, title: str, content: str = ""):
    if title is None or title.strip() == "":
        raise HTTPException(status_code=400, detail="TITLE REQUIRED")
    title = title.strip()
    content = "" if content is None else content

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE memo SET title = ?, content = ? WHERE memo_id = ?",
        (title, content, memo_id),
    )
    conn.commit()
    updated = cur.rowcount
    conn.close()

    if updated == 0:
        raise HTTPException(status_code=404, detail="NOT FOUND")

    return {"memo_id": memo_id, "title": title, "content": content}

# 메모 삭제: memo_id의 메모를 삭제하고 성공 메시지를 반환
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM memo WHERE memo_id = ?", (memo_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="NOT FOUND")

    return {"message": "deleted"}
