import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Request

from dao import note_dao
from router._index_router import root

from module.config_module import config

app = FastAPI()

# 配置CORS中间件
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的跨域源，可以根据需求进行设置，例如 ["http://localhost", "https://example.com"]
    allow_credentials=True,  # 是否允许发送身份验证信息（cookies、HTTP认证）等
    allow_methods=["*"],  # 允许的HTTP方法，可以根据需求进行设置，例如 ["GET", "POST", "PUT", "DELETE"]
    allow_headers=["*"],  # 允许的自定义请求头，可以根据需求进行设置，例如 ["Content-Type", "Authorization"]
)

app.include_router(root)


# 重定向"/index.html"到"/"
@app.get("/")
async def redirect_to_index(request: Request):
    return RedirectResponse(url="/index.html", status_code=301)


app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    note_dao.get_all_note()
    print("docs:http://127.0.0.1:5000/docs")
    uvicorn.run(app, host="127.0.0.1", port=5000)
