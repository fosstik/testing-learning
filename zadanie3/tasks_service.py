from tasks_model import TaskModel

tasks:list = []

class Task:

    def get_all_tasks(self): 
        return tasks
    
    def get_one_task(self, id):
        for item in tasks: 
            if item.id == id: 
                return item
            
    def update_task(self,id,title,complete):
        for item in tasks:
            if(item.id == id):
                if title is not None: 
                    item.title = title
                if(complete is not None):
                    item.complete = complete
                return item

    def create_task(self, title): 
        tasks.append(TaskModel(title=title))

    def delete_task(self, id):
        for index,item in enumerate(tasks):
            if(item.id == id):
               del tasks[index]