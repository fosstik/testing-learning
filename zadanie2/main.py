from fastapi import FastAPI, Query, Path
from posts_service import Post

app = FastAPI()
post_service = Post()

@app.get("/posts")
def get_all_posts():
    all_posts = post_service.get_all_posts()
    return all_posts 

@app.get("/posts/one/{item_id}")
def get_one_post(item_id: str = Path(...)):  
    return post_service.get_one_post(item_id)

@app.post("/posts/create")
def create_post(
    title: str = Query(...), 
    description: str = Query(...), 
    comments: list[str] = Query(...)  
):
    post_service.create_post(title, description, comments)
    return 'Запись создана'

@app.put("/posts/update/{item_id}")
def update_post(
    item_id: str = Path(...), 
    title: str | None = Query(None), 
    description: str | None = Query(None),
    comments: list[str] | None = Query(None)  
):
    post_service.update_posts(item_id, title, description, comments)
    return post_service.get_one_post(item_id) 

@app.delete("/posts/delete/{item_id}")
def delete_post(item_id: str = Path(...)):
    post_service.delete_post(item_id)
    return 'Запись удалена'