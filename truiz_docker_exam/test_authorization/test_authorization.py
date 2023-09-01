from authorization import authorization_check
import time 
# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête


def test_permissions_check():
    time.sleep(5)
    """ test permissions for alice on v1"""
    assert( authorization_check( api_address, api_port, 'v1' , 'alice', 'wonderland', 'I should have access')) == 200

    """ test permissions for alice on v2"""
    assert( authorization_check( api_address, api_port, 'v2','alice', 'wonderland', 'I should have access')) == 200


    """ test permissions for bob on v1"""
    assert( authorization_check( api_address, api_port, 'v1','bob', 'builder', 'I should have access')) == 200

    """ test permissions for bob on v2"""
    assert( authorization_check( api_address, api_port, 'v2' ,'bob', 'builder', 'I should not have access')) == 403
