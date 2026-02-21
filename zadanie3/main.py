from fastapi import FastAPI, HTTPException
from tasks_service import Task

app = FastAPI()
task_service = Task()

@app.get("/tasks")
def get_all_tasks():
    all_tasks = task_service.get_all_tasks()
    return all_tasks 

@app.get("/task/one/{item_id}")
def get_one_task(item_id: str):
    try:
        return task_service.get_one_task(item_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/task/create")
def create_task(title:str):
    task_service.create_task(title)
    return 'Задача создана'

@app.put("/task/update/{item_id}")
def update_task(item_id:str, title:str | None = None, complete:bool | None = False ):
    task_service.update_task(item_id, title, complete)
    return task_service.get_one_task(item_id) 

@app.delete("/task/delete/{item_id}")
def delete_task(item_id:str):
    task_service.delete_task(item_id)
    return 'Задача удалена'



