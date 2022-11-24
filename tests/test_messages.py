import sys
sys.path.insert(1, 'C:/Users/danil/Desktop/telegramShop/bot/')

import pytest

import bot as bot
from bot import messages


@pytest.fixture
def api_mock_data():
    products: dict = {
        {
            'id': 24,
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
            'id': 24,
            'name': 'Tablet',
            'category': 'Tablet',
            'price': 345,
            'characteristics': {
                'RAM': '8gb',
                'Display': '18ich',
                'Storage': '64gb'
            }
        }
    }

    product: dict = {
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
    }

    categories: dict = {
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
    }

    category: dict = {
        {
            'pk': 3,
            'name': 'PCs',
            'url_kwarg': 'pc'
        }
    }

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

    add_to_cart: dict = {
        {
            'pk': 28,
            'name': 'Tablet',
            'price': 345
        }
    }

    del_from_cart: dict = {
        {
            'pk': 24,
            'name': 'CPU',
            'price': 674
        }
    }

    order: dict = {
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

    }

    orders: dict = {
        {
            'pk': 1,
            'order_id': 2,
            'items_count': 5,
            'summary': 243
        },
        {
            'pk': 2,
            'order_id': 4,
            'items_count': 2,
            'summary': 654
        },
        {
            'pk': 3,
            'order_id': 52,
            'items_count': 4,
            'summary': 278
        },
    }

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

    output = messages.products(products['products'])
    expected_lines = len(products['products'].items()) + 1 #  Products count + title line

    assert output
    assert expected_lines == output.count('\n')

def test_product(mocker, api_mock_data):
    product = api_mock_data['product']['product']
    mocker.patch('api_service.get_product', return_value=product)
      

    id = product.keys()[0]
    product = product.values()[0]

    expected_lines = 1 + 1 + len(product['characteristics'].keys()) + 1 + 1 #  Title line + blank + characteristics + black + price
    output = messages.product(1)
    
    assert output
    assert expected_lines == output.count('\n') 

def test_category(mocker, api_mock_data):
    category = api_mock_data['category']

    mocker.patch('api_service.get_category', return_value=category)

    expected_lines = 1 + 1 #  Category + title line
    output = messages.category(category['category'])
    
    assert output
    assert expected_lines == output.count('\n') 

def test_add_to_cart(mocker, api_mock_data):
    add_to_cart = api_mock_data['add_to_cart']

    mocker.patch('api_service.add_to_cart', return_value=add_to_cart)

    expected_lines = 1 + 1 #  Product + title line
    output = messages.add_to_cart(add_to_cart['product'])
    
    assert output
    assert expected_lines == output.count('\n') 

def test_del_from_cart(mocker, api_mock_data):
    del_from_cart = api_mock_data['del_from_cart']

    mocker.patch('api_service.del_from_cart', return_value=del_from_cart)

    expected_lines = 1 + 1 #  Product + title line
    output = messages.del_from_cart(del_from_cart['product'])
    
    assert output
    assert expected_lines == output.count('\n') 

def test_send_cart(mocker, api_mock_data):
    cart = api_mock_data['cart']

    mocker.patch('api_service.get_cart', return_value=cart)

    expected_lines = len(cart['cart']) + 1 #  Cart products + title line
    output = messages.cart(cart['cart'])
    
    assert output
    assert expected_lines == output.count('\n') 

def test_make_order_title():
    expected_lines =  1 #  Only title line
    output = messages.make_order()
    
    assert output
    assert expected_lines == output.count('\n') 

def test_send_order(mocker, api_mock_data):
    order = api_mock_data['order']

    mocker.patch('api_service.get_order', return_value=order)

    expected_lines = len(order['products']) + 1 #  Order products + title line
    output = messages.order(order['order'])
    
    assert output
    assert expected_lines == output.count('\n') 

def test_send_orders(mocker, api_mock_data):
    orders = api_mock_data['orders']

    mocker.patch('api_service.get_orders', return_value=orders)

    expected_lines = 1 + 1 #  Category + title line
    output = messages.orders(orders['orders'])
    
    assert output
    assert expected_lines == output.count('\n') 
