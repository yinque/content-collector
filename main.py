import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import Request

from dao import note_dao
from controller import note_controller

app = FastAPI()

app.include_router(note_controller.api)


# 重定向"/index.html"到"/"
@app.get("/")
async def redirect_to_index(request: Request):
    return RedirectResponse(url="/index.html", status_code=301)


app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    note_dao.get_all_note()
    print("docs:http://127.0.0.1:5000/docs")
    uvicorn.run(app, host="127.0.0.1", port=5000)
