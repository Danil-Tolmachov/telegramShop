
class Token:
    pass

class User:
    pass

def create_user(user_id: int) -> Token:
    pass


def auth_user(user_id: int, token: Token = None) -> User:
    pass


def login_user(user_id: int, token: Token = None, user: User = None) -> User:
    pass


def logout_user(user_id: int, token: Token = None) -> bool:
    pass


def change_user(user_id: int, *args, **kwargs) -> User:
    pass


def get_user(product_id: int, token: Token = None) -> User:
    pass


def test_get_token_users(token: Token) -> list:
    pass


def get_product(product_id: int) -> dict:
    pass


def get_products(page: int) -> list:
    pass


def get_categories() -> list:
    pass


def get_category(category_id: int) -> dict:
    pass


def get_cart(user_id: int, token: Token = None) -> list:
    pass


def add_to_cart(user_id: int, product: int, token: Token = None) -> bool:
    pass


def del_from_cart(user_id: int, product: int, token: Token = None) -> bool:
    pass


def make_order(user_id: int, token: Token = None) -> list:
    pass


def get_order(order_id: int) -> list:
    pass


def get_orders(user_id: int, token: Token = None) -> list:
    pass
