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
            # "title": "Test Title",
            "content": "Test Content",
            "modify_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        content_list = ['龙魂觉醒：我心中沉睡着一条巨龙的魂魄，等待着苏醒的时刻。在古老的神秘洞窟中，我将面对无尽的试炼，唤醒内心深处的龙之力量，以抵挡黑暗势力的侵袭，成为真正的龙魂勇士。', '魔法之剑的宿命：我手握一把传说中的魔法之剑，注入着古老魔法的力量。我是守护正义的勇士，注定要与邪恶势力展开决战。剑刃闪耀着神秘的符文，它将指引我踏上英雄的征程，解开宿命的谜团。', '暗影猎人的咒印：我是暗影猎人，追踪夜幕中的恶魔和堕落。我的身体镌刻着咒印，使我能够穿梭于黑暗之中，释放惩罚的力量。我将迎接血腥的战斗，让邪恶感受我的复仇之刃。', '神圣骑士的审判：我是神圣的骑士，手持神圣之剑，充满正义的怒火。我誓言要保护弱者，驱逐黑暗势力。我的铠甲闪耀着神圣的光芒，敌人将在我面前颤抖，因为审判之刃即将降临。', '黑夜女王的咒术：我是黑夜女王，统御着暗黑之力。黑暗的夜空是我的王国，而我的咒术能够带来毁灭与绝望。我将用黑暗之火燃尽一切，让整个世界沉浸在永恒的黑暗中，只为了满足我那无尽的渴望。']
        for i in content_list:
            note_data["content"] = i
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
