import time
import unittest
from dao import note_dao

class NoteDaoTestCase(unittest.TestCase):
    def test1_create_note(self):
        note = {
            "title": "Test Note",
            "content": "This is a test note",
            "modify_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        affect_row = note_dao.create_note(note)
        print("Create Note - Affected Rows:", affect_row)

    def test2_get_all_notes(self):
        data = note_dao.get_all_note()
        print("Get All Notes - Data:", data)

    def test3_get_note_by_id(self):
        note_id = 1
        data = note_dao.get_note_by_id(note_id)
        print("Get Note by ID - Data:", data)

    def test4_update_note(self):
        note_id = 1
        updates = {
            "title": "Updated Note",
            "content": "This note has been updated",
            "modify_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        affect_row = note_dao.update_note(note_id, updates)
        print("Update Note - Affected Rows:", affect_row)

    def test5_delete_note(self):
        note_id = 1
        affect_row = note_dao.delete_note(note_id)
        print("Delete Note - Affected Rows:", affect_row)

    def test6_reset_table(self):
        table_name = "Note"
        note_dao.reset_table(table_name)
        print("Reset Table - Done")

if __name__ == "__main__":
    unittest.main()
