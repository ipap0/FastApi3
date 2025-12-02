from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from starlette import status
from starlette.responses import JSONResponse

from human import Human

#как бы "база данных"
human_storage = [Human(name='Вася ', age=36), Human(name='Ира',age= 29)]
print(human_storage)


def find_human_by_id(id: str):
    for human in human_storage:
        if str(human.id) == id:
            return human
    return None


def filter_human_by_age(humans, age_from=None, age_to=None) -> list[Human]:
    res = humans
    if age_from is not None:
        res = [h for h in res if h.age >= age_from]
    if age_to is not None:
        res = [h for h in res if h.age <= age_to]
    return res


app = FastAPI()


#заглавная страница
@app.get('/')
def index():
    return {'message': 'начало'}


#получение всех людей                        GET
@app.get('/humans')
def get_humans(age_from: Optional[int] = None, age_to: Optional[int] = None):
    print(age_from, age_to)
    humans = filter_human_by_age(human_storage, age_from, age_to)
    return humans


#получение одного конкретного человека       GET
@app.get('/humans/{id}')
def get_one_human(id: str):
    print(id)
    h = find_human_by_id(id)
    if h is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Нет такого человека'})
    return h
#добавление человека                         POST
@app.post('/humans')
def add_one_human(new_h : Human = Body()):
    print(new_h)
    human_storage.append(new_h)
    return {'message': 'Добавлен человек', 'human':new_h}

#удаление одного конкретного человека        DEL
@app.delete('/humans')
def delete_human(id: str):
    h = find_human_by_id(id)
    if h is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Нет такого человека'})
    human_storage.remove(h)
    return {'message': 'Удален человек', 'human':h}
#редактирование человека                     PUT
@app.route('/humans', methods=['PUT'])
def edit_human(h : Human = Body()):
    print(f'пришел объект {h}')
    old_h = find_human_by_id(h.id)
    if old_h is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Нет такого человека'})
    else:
        old_h.name = h.name
        old_h.age  = h.age
    return {'message': 'Изменен человек', 'human':h}

@app.get('/celebrate/{id}')
def celebrate(id: str):
    h = find_human_by_id(id)
    if h is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Нет такого человека'})
    s = h.celebrate_birtsday()
    return {'message':s, 'human': h}