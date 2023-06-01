import uvicorn
from fastapi import FastAPI
from dao import note_dao

app = FastAPI()

from pydantic import BaseModel


# 定义笔记模型
class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: str
    content: str


# 创建笔记
@app.post("/notes")
def create_note(note: NoteCreate):
    created_note = note_dao.create_note({
        "title": note.title,
        "content": note.content
    })
    return created_note


# 获取所有笔记
@app.get("/notes")
def get_all_notes():
    return note_dao.get_all_note()


# 根据ID获取笔记
@app.get("/notes/{note_id}")
def get_note_by_id(note_id: int):
    return note_dao.get_note_by_id(note_id)


# 更新笔记
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    updates = {
        "title": note.title,
        "content": note.content
    }
    note_dao.update_note(note_id, updates)
    return {"message": "Note updated successfully"}



if __name__ == "__main__":
    note_dao.get_all_note()
    print("docs:http://127.0.0.1:5000/docs")
    uvicorn.run(app, host="127.0.0.1", port=5000)
