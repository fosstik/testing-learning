from fastapi import FastAPI
from posts_service import Post

app = FastAPI()
post_service = Post()

@app.get("/posts")
def get_all_posts():
    all_posts = post_service.get_all_posts()
    return all_posts 

@app.get("/posts/one/{item_id}")
def get_one_post(item_id: str):
    return post_service.get_one_post(item_id)

@app.post("/posts/create")
def create_post(title:str, description:str, comments:list[str]):
    post_service.create_post(title, description, comments)
    return 'Запись создана'

@app.put("/posts/update/{item_id}")
def update_post(item_id:str, title:str | None = None, description:str | None = None, comments:list[str] | None = None):
    post_service.update_posts(item_id, title, description, comments)
    return post_service.get_one_post(item_id) 

@app.delete("/posts/delete/{item_id}")
def delete_post(item_id:str):
    post_service.delete_post(item_id)
    return 'Запись удалена'



