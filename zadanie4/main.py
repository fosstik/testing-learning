from fastapi import FastAPI, Query, Path,HTTPException
from product_service import Product

app = FastAPI()
product_service = Product()

@app.get("/products")
def get_all_get_one_products():
    all_products = product_service.get_all_products()
    return all_products

@app.get("/products/one/{item_id}")
def get_one_product(item_id: str = Path(...)):  
    return product_service.get_one_product(item_id)

@app.post("/products/create")
def create_product(
    title: str = Query(...), 
    description: str = Query(...), 
    reviews: list[str] = Query(...), 
    rating: int = Query(...)
):
    try:
        product_service.create_product(title, description, reviews, rating)
        return 'Товар создан'
    except ValueError:
        raise HTTPException(status_code=404, detail="Error")


@app.put("/products/update/{item_id}")
def update_product(
    item_id: str = Path(...), 
    title: str | None = Query(None), 
    description: str | None = Query(None),
    reviews: list[str] | None = Query(None), 
    rating: int | None = Query(None), 
):
    try:
        if(rating > 5):  
            return "Оценка должна быть меньше или равна 5"
        product_service.update_product(item_id, title, description, reviews, rating)
        return product_service.get_one_product(item_id) 
    except ValueError:
        raise HTTPException(status_code=404, detail="Error")

@app.delete("/products/delete/{item_id}")
def delete_product(item_id: str = Path(...)):
    product_service.delete_product(item_id)
    return 'Продукт удалена'