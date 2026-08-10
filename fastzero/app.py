from http import HTTPStatus

from fastapi import FastAPI

from fastzero.schemas import Message

app = FastAPI(title='Little API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'msg': 'Ola mundo!'}
