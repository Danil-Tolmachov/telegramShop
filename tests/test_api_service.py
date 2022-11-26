import sys
sys.path.insert(1, 'C:/Users/danil/Desktop/telegramShop/bot/')

import pytest
import api_service as api



@pytest.fixture
def user_data():
    user_id: int = 470994972
    token: str = '559b171b5875bdd9a155030d5d3446b39768fab8'

    data = {
        'user_id': user_id,
        'token': token,
    }

    return data


@pytest.fixture
def moker_data():
    cart: dict = {
        {
            'pk': 1,
            'name': 'Laptop',
            'price': 243
        },
        {
            'pk': 2,
            'name': 'Smartphone',
            'price': 243
        }
    }

    data = {
        'cart': cart
    }

    return data



def test_create_user(user_data):
    user_id = user_data['user_id']

    token = api.create_user(user_id)
    assert type(token) is str

    assert token == api.create_user(user_id)


def test_auth_user(user_data):
    user_id = user_data['user_id']
    token = user_data['token']

    user1 = api.auth_user(user_id, token=token)
    assert user1
    assert user_id not in user1.sessions

    user2 = api.auth_user(user_id)
    assert user2

    assert user1 != user2

    with pytest.raises(Exception) as exc_info:
        assert api.auth_user(user_id, token + 'dsasfw')

    assert str(exc_info.value) == "Token doesn't exist"


def test_login_user(user_data):
    user_id = user_data['user_id']
    token = user_data['token']

    user1 = api.login_user(user_id, token=token)
    assert user1
    assert user_id in user1.sessions

    with pytest.raises(Exception) as exc_info1:
        assert api.login_user(user_id)

    assert str(exc_info1.value) == 'Already logged in'

    with pytest.raises(Exception) as exc_info2:
        reversed_id = int(str(user_id)[::-1])
        assert api.login_user(reversed_id)

    assert str(exc_info2.value) == 'Another user already logged in'


def test_logout_user(user_data):
    user_id = user_data['user_id']

    logout = api.logout_user(user_id)
    assert logout == True

    with pytest.raises(Exception) as exc_info:
        assert api.logout_user(user_id)

    assert str(exc_info.value) == 'You are already logged out'


def test_change_user(user_data):
    user_id = user_data['user_id']
    token = user_data['token']

    address = 'some address'

    user = api.change_user(user_id, token=token, address=address)
    assert user.address == address

    with pytest.raises(Exception) as exc_info:
        assert api.change_user(user_id, token=token)

    assert str(exc_info.value) == 'No fields to change'


def test_get_user(user_data):
    user_id = user_data['user_id']

    user = api.get_user(user_id)
    user = user['user']
    assert type(user) is User

    with pytest.raises(Exception) as exc_info:
        assert api.get_user(user_id)

    assert str(exc_info.value) == "User doesn't exist"


def test_get_token_users(user_data):
    token = user_data['token']

    with pytest.raises(Exception) as exc_info:
        assert api.get_token_users(token + 'sdawdw')

    assert str(exc_info.value) == "Token doesn't exist"

    users = api.get_token_users(token)
    users = users['users']
    assert type(users) is dict

    user = users.items()[0]
    assert type(user) is User 



def test_get_products():
    for page in range(5):
        result: dict = api.get_products(page)

        assert result['products']
        assert result is not None and type(result) is dict


def test_get_product():
    for product_id in range(5):
        result: dict = api.get_product(product_id)

        assert result['product']
        assert result is not None and type(result) is dict
    

def test_get_categories():
    result: dict = api.get_categories()

    assert result['categories']
    assert result is not None and type(result) is dict
    

def test_get_category():
    for category_id in range(5):
        result: dict = api.get_category(category_id)

        assert result['category']
        assert result is not None and type(result) is dict


def test_get_cart():
    for user_id in range(5):
        result: dict = api.get_cart(user_id)

        assert result['cart']
        assert result is not None and type(result) is dict


def test_add_to_cart():
    user_id = 1
    products_count = len(api.get_cart(user_id)['cart'].items())

    for product in range(5):
        result: dict = api.add_to_cart(user_id, product)

        assert result is not None and type(result) is dict

        if 'errors' not in result:
            assert 'product' in result
            
            actual_products_count = len(api.get_cart(user_id)['cart'].items())
            products_count += 1
            assert products_count == actual_products_count


def test_del_from_cart():
    user_id = 1
    products_count = len(api.get_cart(user_id)['cart'].items())

    for product in range(5):
        result: dict = api.del_from_cart(user_id, product)

        assert result is not None and type(result) is dict

        if not result['errors']:
            assert result['product']

            actual_products_count = len(api.get_cart(user_id)['cart'].items())
            products_count -= 1
            assert products_count == actual_products_count


def test_make_order():
    for user_id in range(5):
        result: dict = api.make_order(user_id)

        assert result['order']
        assert result is not None and type(result) is dict


def test_get_order():
    for order_id in range(5):
        result: dict = api.get_order(order_id)

        assert result['order']
        assert result is not None and type(result) is dict


def test_get_orders():
    for user_id in range(5):
        result: dict = api.get_orders(user_id)

        assert result is not None and type(result) is dict
        assert result['orders']