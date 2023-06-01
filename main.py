import uvicorn
from fastapi import FastAPI
from dao import note_dao
from controller import note_controller

app = FastAPI()

app.include_router(note_controller.api)


if __name__ == "__main__":
    note_dao.get_all_note()
    print("docs:http://127.0.0.1:5000/docs")
    uvicorn.run(app, host="127.0.0.1", port=5000)
