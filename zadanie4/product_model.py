import uuid 

class ProductModel:
    id:str
    title:str
    description:str
    reviews:list[str]
    rating:int

    def __init__(self, title, description, reviews, rating): 
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.reviews = reviews
        self.rating = rating