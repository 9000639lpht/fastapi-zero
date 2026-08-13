from http import HTTPStatus

from fastapi import FastAPI

from fastzero.schemas import Message, Userdb, UserPublic, UserSchema

app = FastAPI(title='Little API')

db = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'msg': 'Ola mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema) -> UserSchema:
    user_with_id = Userdb(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(db) + 1,
    )

    db.append(user_with_id)

    return user_with_id
