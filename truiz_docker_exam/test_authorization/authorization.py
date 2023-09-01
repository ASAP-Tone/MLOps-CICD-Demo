import os
import requests
from datetime import datetime

# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête

def authorization_check( api_address : str, port : int , version : str, username : str, password : str, sentence : str ) -> str: 

    try: 
        r = requests.get(
            url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version =version),
            params= {
                'username': username, 
                'password': password, 
                'sentence' : sentence
            }
        )
        output = '''
            ==================================
            Authorization Test - Date {date}
            =================================
            request done at "{version}/sentiment"
            | username={username}
            | password={password}
            | sentence={sentence}
            actual restult = {status_code}
            ==>  {test_status}
            '''
            # query status
        status_code = r.status_code
        # display the results
        if status_code == 200:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'
        print(output.format(date = datetime.now() ,status_code=status_code, test_status=test_status, version=version,  
                            username = username, password=password, sentence=sentence))
        test_output = output.format(date = datetime.now() ,status_code=status_code, test_status=test_status, version=version,  
                            username = username, password=password, sentence=sentence)
    except:
        print( 'Could not reach server')
        status_code = -1 
        test_output = "ERROR: Could not reach server" 
    
    # printing in a file
    if os.environ.get('LOG') == '1':
        with open('/home/log_folder/api_test.log', 'a') as file:
            file.write(test_output)
    
    return status_code


# if __name__ == "__main__":

#     test_permissions( api_address, api_port, 'alice', 'wonderland')
#     test_permissions( api_address, api_port, 'bob', 'builder')
#     test_permissions( api_address, api_port, 'tony', 'ruiz')



    