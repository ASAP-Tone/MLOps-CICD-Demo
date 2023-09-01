from content import content_check
import time 
# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête


def test_permissions_check():
    time.sleep(5)
    """ test permissions for positive permissions on v1"""
    assert( content_check( api_address, api_port, 'v1' , 'alice', 'wonderland', 'I love everything')) == 'positive'

    # """ test for negative permissions on v1"""
    assert( content_check( api_address, api_port, 'v1','bob', 'builder', 'I hate everything')) == 'negative'


    # """ test permissions for positive positive sentiment on v2"""
    assert( content_check( api_address, api_port, 'v1','bob', 'builder', 'I love everything')) == 'positive'

    # """ test permissions for negative sentiment on v2"""
    assert( content_check( api_address, api_port, 'v2' ,'alice', 'wonderland', 'I hate everything', )) == 'negative'
