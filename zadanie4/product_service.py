from product_model import ProductModel


products:list = []

class Product:

    def get_all_products(self): 
        return products
    
    def get_one_product(self, id):
        for item in products: 
            if item.id == id: 
                return item
            
    def update_product(self,id,title,description, reviews, rating):
        for item in products:
            if(item.id == id):
                if title is not None: 
                    item.title = title
                if(description is not None):
                    item.description = description
                if(reviews is not None):
                    item.reviews = reviews
                if(rating is not None):
                    item.rating = rating
                return item

    def create_product(self, title, description, reviews, rating): 
        products.append(ProductModel(title=title, description=description, reviews=reviews, rating=rating))

    def delete_product(self, id):
        for index,item in enumerate(products):
            if(item.id == id):
               del products[index]