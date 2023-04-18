from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (create_todo_data, delete_todo_data, fetch_all_todos,
                      fetch_one_todo, update_todo_data)
from model import Todo

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(CORSMiddleware, 
                   allow_origins=origins, 
                   allow_credentials=True, 
                   allow_methods=['*'], 
                   allow_headers=['*'])

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get('/api/todo/{title}', response_model=Todo)
async def get_todo_by_title(title: int):
    response = await fetch_one_todo(title)
    return response

@app.post('/api/todo')
async def create_todo(todo: Todo):
    response = await create_todo_data(todo.dict())
    if response:
        return response
    
    raise HTTPException(status_code=400, detail='Todo already exists')

@app.put('/api/todo/{title}')
async def update_todo_by_title(title: int, data):
    response = await update_todo_data(title, data)
    return response

@app.delete('/api/todo/{title}')
async def delete_todo_by_title(title: int):
    response = await delete_todo_data(title)
    return response
    