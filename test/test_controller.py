import time
import unittest
import httpx

from dao import note_dao


class TestNoteAPI(unittest.TestCase):

    base_url = "http://127.0.0.1:5000"  # 指定 baseurl

    def send_request(self, method, path, json=None):
        url = f"{self.base_url}{path}"
        response = httpx.request(method, url, json=json)
        return response.json()

    def test1_create_note(self):
        note_data = {
            "title": "Test Title",
            "content": "Test Content",
            "modify_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        response = self.send_request("POST", "/notes/", json=note_data)
        print(response)

    def test2_get_all_notes(self):
        response = self.send_request("GET", "/notes/")
        print(response)

    def test3_get_note_by_id(self):
        note_id = 1
        response = self.send_request("GET", f"/notes/{note_id}")
        print(response)

    def test4_update_note(self):
        note_id = 1
        note_data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "modify_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        response = self.send_request("PUT", f"/notes/{note_id}", json=note_data)
        print(response)

    def test5_delete_note(self):
        note_id = 1
        response = self.send_request("DELETE", f"/notes/{note_id}")
        print(response)

    def test6_reset_table(self):
        note_dao.reset_table()



if __name__ == "__main__":
    unittest.main()
