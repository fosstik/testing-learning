import uuid

class TaskModel:
    id:str
    title:str
    complete:bool
    def __init__(self, title): 
        self.id = str(uuid.uuid4())
        self.title = title
        self.complete = False