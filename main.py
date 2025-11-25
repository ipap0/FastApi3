from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from human import Human

#как бы "база данных"
human_storage = [ Human('Вася ',36), Human('Ира', 29)]
print(human_storage)
def find_human_by_id(id: str):
    for human in human_storage:
        if str(human.id) == id:
            return human
    return None

app = FastAPI()

#заглавная страница
@app.get('/')
def index():
    return {'message': 'начало'}
#получение всех людей                        GET
@app.get('/humans')
def get_humans():
    return human_storage
#получение одного конкретного человека       GET
@app.get('/humans/{id}')
def get_one_human(id: str):
    print(id)
    h = find_human_by_id(id)
    if h is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,  content={'message': 'Нет такого человека'})
    return h
#добавление человека                         POST

#удаление одного конкретного человека        DEL

#редактирование человека                     PUT
