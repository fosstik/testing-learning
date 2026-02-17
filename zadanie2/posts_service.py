import uuid
from posts_model import PostModel
from fastapi import HTTPException, status

posts:list = []

class Post:
    def get_all_posts(self): 
        return posts
    
    def get_one_post(self, id):
        for item in posts: 
            if item.id == id: 
                return item
        raise HTTPException(status_code=404, detail="Пост не найден")

    def update_posts(self,id,title,description, comments):
        for item in posts:
            if(item.id == id):
                if title is not None: 
                    item.title = title
                if(description is not None):
                    item.description = description
                if(comments is not None):
                    item.comments = comments
                return item

    def create_post(self, title, description, comments): 
        post = PostModel(title=title, description=description, comments=comments)
        posts.append(post)
        return post

    def delete_post(self, id):
        for index,item in enumerate(posts):
            if(item.id == id):
                del posts[index]
                return
        raise HTTPException(status_code=404, detail="Пост не найден")