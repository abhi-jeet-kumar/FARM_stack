from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return 1

@app.get('/api/todo/{id}')
async def get_todo_by_id(id: int):
    return id

@app.post('/api/todo')
async def create_todo(todo):
    return todo

@app.update('/api/todo/{id}')
async def update_todo_by_id(id: int, data):
    return data

@app.delete('/api/todo/{id}')
async def delete_todo_by_id(id: int):
    return id
    