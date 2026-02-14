import uuid
from posts_model import PostModel

posts:list = []

class Post:

    def get_all_posts(self): 
        return posts
    
    def get_one_post(self, id):
        for item in posts: 
            if item.id == id: 
                return item
            
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
        posts.append(PostModel(title=title, description=description, comments=comments))

    def delete_post(self, id):
        for index,item in enumerate(posts):
            if(item.id == id):
               del posts[index]