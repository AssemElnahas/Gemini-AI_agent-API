from datetime import datetime

def get_current_time() -> str:
    """
    Return the current date and time
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def search_product(product_name: str)->dict:
    """
    Search for a product in our mock product database
    """
    products = {
        "nike air max": {
            "name": "Nike Air Max",
            "price": 120,
            "stock": 5,
            "sizes": [40, 41, 42, 43, 44] },
        "adidas ultraboost": {
            "name": "Adidas Ultraboost",
            "price": 150,
            "stock": 3,
            "sizes": [41, 42, 43] },
        "puma rs-x": {
            "name": "Puma RS-X",
            "price": 100,
            "stock": 8,
            "sizes": [39, 40, 41, 42, 43]
            }
        }
    product = products.get(product_name.lower())
    
    if product:
        return{
            "success": True,
            "Product": product
        }
    return {
        "success": False,
        "Product": product
    }

def check_stock(product_name : str)-> dict:
    """
    Check the stock of a product
    """
    result = search_product(product_name)
    
    if not result["success"]:
        return result
    
    product = result['product']
    
    return{
        "product":product["name"],
        "stock": product["stock"],
        "available": product["stock"]>0
    }
def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total price
    """
    return price* quantity
    
    