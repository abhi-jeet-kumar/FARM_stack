from model import Todo

#this is the mongoDB driver
import motor.motor_asyncio as mongo_db_driver

uri = ""

client = mongo_db_driver.AsyncIOMotorClient(uri)

database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
        
    return todos

async def create_todo_data(todo: Todo):
    todos = await fetch_all_todos()
    for todo_existing in dict(todos):
        if todo_existing['title'] == todo.title:
            return {"error": "Todo with title: {} already exists".format(todo.title)}
    result = await collection.insert_one(todo.dict())
    return todo

async def update_todo_data(title: str, description: str):
    query = {"title": title}
    newvalues = {"$set": {"description": description}}
    await collection.update_one(query, newvalues)
    document = collection.find_one(query)
    return document

async def delete_todo_data(title: str):
    await collection.delete_one({"title": title})
    return {"message": "Todo with title: {} deleted successfully!".format(title)}
    