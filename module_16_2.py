from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()


@app.get("/")                                     #get запрос и выполнении функции при его вызове
async def welcome() -> dict:                      #возвращаемый тип данных - словарь
    return {"message": "Hello World"}             #

@app.get("/user/admin")                                        #get запрос и выполнении функции при его вызове
async def news() -> dict:                                      #возвращаемый тип данных - словарь
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{user_id}")                                    #get запрос и выполнении функции при его вызове
async def user_id(user_id: int = Path(ge=1, le=100, description="Enter User ID")) -> dict:     #возвращаемый тип данных - словарь
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_paginator(username: str = Path(min_length=5,max_length=20, description="Enter username")
                         , age: int = Path(ge=18,le=120,description="Enter age")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username},Возраст: {age}"}




#запрсы
# Get   - адрес в строке ? переменная=значение
# Post - формы - офрмитьзаказ в магазине
# Put - заменить
# Delete - удалить