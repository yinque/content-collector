from functools import wraps
from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter
from dao import note_dao
from controller.util.response_format import success_message, fail_message


# 定义笔记模型
class NoteCreate(BaseModel):
    title: Optional[str] = None
    content: str
    modify_time: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: str
    modify_time: str


api = APIRouter(prefix="/notes")


# sql执行错误处理
def handle_sql_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return fail_message("sql执行失败：" + str(e))

    return wrapper


# 创建笔记
@api.post("/")
@handle_sql_exception
def create_note(note: NoteCreate):
    # 内容判断
    if not note.content:
        return fail_message("内容不能为空")
    # 标题补充
    if not note.title:
        note.title = note.content[:50]+"..."
    # 插入数据
    affect_row = note_dao.create_note(dict(note))
    if affect_row == 1:
        return success_message("添加成功")
    else:
        return fail_message("添加失败，原因我怎么知道啊？数据库影响行数为零就是插入失败了啊")


# 获取所有笔记
@api.get("/")
@handle_sql_exception
def get_all_notes():
    data = note_dao.get_all_note()
    return success_message("获取成功", data=data)


# 根据ID获取笔记
@api.get("/{note_id}")
@handle_sql_exception
def get_note_by_id(note_id: int):
    data = note_dao.get_note_by_id(note_id)
    if data:
        return success_message("获取成功", data=data)
    else:
        return fail_message("获取失败，id不存在")


# 更新笔记
@api.put("/{note_id}")
@handle_sql_exception
def update_note(note_id: int, note: NoteUpdate):
    # 内容判断
    if not note.content:
        return fail_message("内容不能为空")
    # 标题补充
    if not note.title:
        note.title = note.content[:50]+"..."
    # 修改数据
    affect_row = note_dao.update_note(note_id, dict(note))
    if affect_row == 1:
        return success_message("更新成功")
    else:
        return fail_message("更新失败")


@api.delete("/{note_id}")
@handle_sql_exception
def delete_note(note_id: int):
    affect_row = note_dao.delete_note(note_id)
    if affect_row == 1:
        return success_message("删除成功")
    else:
        return fail_message("删除失败")
