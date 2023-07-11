import json
import os

# 默认配置
config = {
    "token": "0000000000:xxx",
}

# 配置文件存在判断
if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        f.write(json.dumps(config, indent=4))
    raise Exception("配置文件未找到，已自动创建，请填写。")
# 打开配置文件
with open('config.json', "r") as f:
    c = f.read()
    try:
        c = json.loads(c)
    except:
        raise Exception("载入配置错误")
    config.update(c)
