import sys
sys.path.insert(1, 'C:/Users/danil/Desktop/telegramShop/bot/')

import pytest

import bot as bot
from bot import messages


@pytest.fixture
def api_mock_data():
    products: list = [
        {
            'pk': 24,
            'name': 'Tablet',
            'category': 'Tablet',
            'price': 345,
            'characteristics': {
                'RAM': '8gb',
                'Display': '18ich',
                'Storage': '64gb'
            }
        },
        {
            'pk': 24,
            'name': 'Tablet',
            'category': 'Tablet',
            'price': 345,
            'characteristics': {
                'RAM': '8gb',
                'Display': '18ich',
                'Storage': '64gb'
            }
        }
    ]

    product: dict = {
            'pk': 24,
            'name': 'Tablet',
            'category': 'Tablet',
            'price': 345,
            'characteristics': {
                'RAM': '8gb',
                'Display': '18ich',
                'Storage': '64gb'
                }
        }

    categories: list = [
        {
            'pk': 56,
            'name': 'PCs',
            'url_kwarg': 'pc'
        },
        {
            'pk': 2,
            'name': 'PSUs',
            'url_kwarg': 'pcu'
        },
        {
            'pk': 35,
            'name': 'Cases',
            'url_kwarg': 'case'
        }
    ]

    category: dict = {
            'pk': 3,
            'name': 'PCs',
            'url_kwarg': 'pc'
        }

    cart: list = [
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
    ]

    add_to_cart: dict = {
            'pk': 28,
            'name': 'Tablet',
            'price': 345
        }

    del_from_cart: dict = {
            'pk': 24,
            'name': 'CPU',
            'price': 674
        }

    order: list = [
        {
            'pk': 1,
            'name': 'Laptop',
            'price': 243
        },
        {
            'pk': 76,
            'name': 'Tablet',
            'price': 678
        },
        {
            'pk': 53,
            'name': 'Smartphone',
            'price': 654
        },
    ]

    orders: list = [
        {
            'pk': 2,
            'items_count': 5,
            'summary': 243
        },
        {
            'pk': 4,
            'items_count': 2,
            'summary': 654
        },
        {
            'pk': 52,
            'items_count': 4,
            'summary': 278
        },
    ]

    data: dict = {
        'products': products,
        'product': product,
        'categories': categories,
        'category': category,
        'cart': cart,
        'add_to_cart': add_to_cart,
        'del_from_cart': del_from_cart,
        'order': order,
        'orders': orders
    }

    return data



def test_welcome(mocker, api_mock_data):
    products = api_mock_data['products']

    mocker.patch('api_service.get_products', return_value=products)

    output = messages.welcome()
    assert output


def test_products(mocker, api_mock_data):
    products = api_mock_data['products']

    mocker.patch('api_service.get_products', return_value=products)

    output = messages.products(1)
    expected_lines = len(products) #  Products count
    assert output
    assert expected_lines == output.count('\n')

    output = messages.products(1, title='Products:\n')
    expected_lines = len(products) + 1 #  Products count + title
    assert output
    assert expected_lines == output.count('\n')


def test_product(mocker, api_mock_data):
    product = api_mock_data['product']
    mocker.patch('api_service.get_product', return_value=product)

    expected_lines = 1 + len(product['characteristics']) #  Product title line + characteristics
    output = messages.product(1, title='')
    assert output
    assert expected_lines == output.count('\n') 
 

    expected_lines = 1 + 1 + len(product['characteristics']) #  Title line + product title line + blank + characteristics
    output = messages.product(1, title='Product:\n')
    assert output
    assert expected_lines == output.count('\n') 


def test_category(mocker, api_mock_data):
    category = api_mock_data['category']

    mocker.patch('api_service.get_category', return_value=category)

    expected_lines = len(category) #  Category fields
    output = messages.category(2)
    assert output
    assert expected_lines == output.count('\n') 

    expected_lines = len(category) + 1 #  Category fields + title
    output = messages.category(2, title='Category\n')
    assert output
    assert expected_lines == output.count('\n') 


def test_add_to_cart(mocker, api_mock_data):
    add_to_cart = api_mock_data['add_to_cart']

    mocker.patch('api_service.get_product', return_value=add_to_cart)

    expected_lines = 1 #  Title: product
    output = messages.add_to_cart(2)
    
    assert output
    assert expected_lines == output.count('\n') 


def test_del_from_cart(mocker, api_mock_data):
    del_from_cart = api_mock_data['del_from_cart']

    mocker.patch('api_service.get_product', return_value=del_from_cart)

    expected_lines = 1 #  Title: product
    output = messages.del_from_cart(4)

    assert output
    assert expected_lines == output.count('\n') 


def test_cart(mocker, api_mock_data):
    cart = api_mock_data['cart']

    mocker.patch('api_service.get_cart', return_value=cart)

    expected_lines = len(cart) #  Cart products 
    output = messages.cart(2)
    assert output
    assert expected_lines == output.count('\n') 

    expected_lines = len(cart) + 1 #  Cart products + title
    output = messages.cart(2, title='Cart\n')
    assert output
    assert expected_lines == output.count('\n') 


def test_order(mocker, api_mock_data):
    order = api_mock_data['order']

    mocker.patch('api_service.get_order', return_value=order)

    expected_lines = len(order) #  Order products
    output = messages.order(order_id=1)
    assert output
    assert expected_lines == output.count('\n') 

    expected_lines = len(order) + 1 #  Order products + title
    output = messages.order(order_id=1, title='Order\n')
    assert output
    assert expected_lines == output.count('\n') 


def test_orders(mocker, api_mock_data):
    orders = api_mock_data['orders']

    mocker.patch('api_service.get_orders', return_value=orders)

    expected_lines = len(orders) #  Orders
    output = messages.orders(1)
    assert output
    assert expected_lines == output.count('\n') 

    expected_lines = len(orders) + 1 #  Orders + title
    output = messages.orders(1, title='Orders\n')
    assert output
    assert expected_lines == output.count('\n') 
