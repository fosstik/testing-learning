import uuid

class PostModel:
    id:str
    title:str
    description:str
    comments:list[str]

    def __init__(self, title, description, comments): 
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.comments = comments