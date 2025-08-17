from fastapi import APIRouter
from pydantic import BaseModel

login_router  = APIRouter()

class User(BaseModel):
    login:str
    password:str

@login_router.post('/login')
def login(user:User):
    print(f'user is {user} and password is {type(user)}')
    if user.login.lower()=='test' and user.password.lower() == 'test':
        return 'SUCCESS'
    else:
        return 'FAIL'