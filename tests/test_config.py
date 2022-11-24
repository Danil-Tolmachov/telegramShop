import sys
sys.path.insert(1, 'C:/Users/danil/Desktop/telegramShop/bot/')

import pytest
import requests
import config



def test_bot_token():
    token = config.BOT_API_TOKEN
    token_validation_url = f'https://api.telegram.org/bot{token}/getMe'

    responce = requests.get(token_validation_url)
    assert responce.ok


def test_shop_api_key():
    pass #  assert config.SHOP_API_KEY


def test_shop_api_call():
    pass #  assert config.SHOP_API_CALL