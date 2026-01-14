-- Memo App 프로젝트 데이터베이스 관리 및 테스트 SQL

-- [1] 테이블 초기화
-- 기존 테이블을 삭제하고 새로 만들고 싶을 때 사용
DROP TABLE IF EXISTS memo;

-- [2] 테이블 생성
-- main.py에서 자동으로 생성되지만, 구조 파악을 위해 명시
CREATE TABLE IF NOT EXISTS memo (
    memo_id INTEGER PRIMARY KEY AUTOINCREMENT, -- 고유 ID (자동 증가)
    title TEXT NOT NULL,                       -- 제목 (필수)
    content TEXT                               -- 내용 (선택)
);

-- [3] 데이터 조회
-- 프론트엔드에서 추가한 데이터가 잘 들어왔는지 확인하는 명령어

-- 3-1. 모든 메모 조회
SELECT * FROM memo;

-- 3-2. 최신순 조회
SELECT * FROM memo ORDER BY memo_id DESC;

-- 3-3. 데이터 개수 확인
SELECT COUNT(*) FROM memo;

-- 3-4. 특정 제목 검색
SELECT * FROM memo WHERE title LIKE '%테스트%';

-- [4] 테스트 데이터 삽입
-- 프론트엔드 연결 전, 백엔드 API(GET /memos)가 잘 작동하는지 확인할 때 사용
INSERT INTO memo (title, content) VALUES ('첫 번째 메모', 'SQL에서 직접 넣은 데이터입니다.');
INSERT INTO memo (title, content) VALUES ('FastAPI 테스트', '데이터가 잘 조회되나요?');
INSERT INTO memo (title, content) VALUES ('쇼핑 목록', '우유, 계란, 사과');

-- [5] 데이터 수정 및 삭제
-- 잘못 들어간 데이터를 수동으로 고칠 때 사용

-- 5-1. 특정 메모(예: 1번) 내용 수정
UPDATE memo
SET content = '내용이 수정되었습니다.',
    title = '수정된 제목'
WHERE memo_id = 1;

-- 5-2. 특정 메모(예: 1번) 삭제
DELETE FROM memo WHERE memo_id = 1;

-- 5-3. 테이블 비우기 (주의: 모든 데이터 삭제)
DELETE FROM memo;