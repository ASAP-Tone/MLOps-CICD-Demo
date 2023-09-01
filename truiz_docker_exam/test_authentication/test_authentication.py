from authentication import authentication_check
from datetime import datetime 
import time
# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête


def test_authentication_check():
    time.sleep(10)
    """ test authentication for alice"""
    assert( authentication_check( api_address, api_port, 'alice', 'wonderland')) == 200

    """ test authentication for bob"""
    assert( authentication_check( api_address, api_port, 'bob', 'builder')) == 200

    """ test authentication for tony"""
    assert( authentication_check( api_address, api_port, 'tony', 'ruiz')) == 403


    