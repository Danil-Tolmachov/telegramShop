import api_service as api

class Token():
    pass


def welcome() -> str:
    message = 'Hey, welcome in our shop'
    return message


def products(page: int, title='') -> str:
    products = api.get_products(page=page)

    message = title
    for product in products:
        message += f"{product['pk']}. {product['name']}: {product['price']}\n"

    return message


def product(id: int, title='') -> str:
    product = api.get_product(id)
    message = title
    message += f"{product['pk']}. {product['name']}: ${product['price']}\n"

    for key, field in product['characteristics'].items():
        message += f"{key}: {field}\n"

    return message


def category(category: str, title="") -> str:
    category = api.get_category(category)
    message = title
    
    for key, field in category.items():
        message += f"{key}: {field}\n"

    return message


def add_to_cart(product_id: int) -> str:
    product = api.get_product(product_id)
    print(product)
    message = f"Added to cart: {product['name']}\n"
    return message


def del_from_cart(product_id: int) -> str:
    product = api.get_product(product_id)
    message = f"Deleted from cart: {product['name']}\n"
    return message


def cart(user_id: int, token: str = Token, title='') -> str:
    cart = api.get_cart(user_id, token=token)

    message = title

    for product in cart:
        message += f"{product['pk']}. {product['name']}: {product['price']}\n"

    return message

def order(order_id: int, title='') -> str:
    order = api.get_order(order_id)
    
    message = title

    for product in order:
        message += f"{product['pk']}. {product['name']}: {product['price']}\n"

    return message


def orders(user_id: int, title='') -> str:
    orders = api.get_orders(user_id)
    
    message = title

    for order in orders:
        message += f"{order['pk']}. {order['items_count']}: {order['summary']}\n"

    return message
