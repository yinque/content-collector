from dao.util.dict_to_sql import dict_to_update_sql, dict_to_create_sql
from dao.util.connector import get_cursor


def create_note(note: dict):
    with get_cursor() as cursor:
        param = dict_to_create_sql(note)
        sql = f"INSERT INTO Note {param[0]} VALUES {param[1]}"
        values = param[2]
        cursor.execute(sql, values)
        return cursor.rowcount


def get_all_note():
    with get_cursor() as cursor:
        sql = "SELECT * FROM Note"
        cursor.execute(sql)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        return data


def get_note_by_id(note_id):
    with get_cursor() as cursor:
        sql = f"SELECT * FROM Note WHERE id = ?"
        cursor.execute(sql, (note_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_note(note_id, updates):
    with get_cursor() as cursor:
        param = dict_to_update_sql(updates)
        sql = f"UPDATE Note SET {param[0]} WHERE id = ?"
        values = param[1] + (note_id,)
        cursor.execute(sql, values)


def delete_note(note_id):
    with get_cursor() as cursor:
        sql = "DELETE FROM Note WHERE id = ?"
        cursor.execute(sql, (note_id,))


def reset_table(table_name="Note"):
    with get_cursor() as cursor:
        cursor.execute(f"DELETE FROM {table_name}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")
