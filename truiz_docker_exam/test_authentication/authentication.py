import os
import requests
from datetime import datetime
# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête


def authentication_check( api_address, port , username, password): 
    try: 
        r = requests.get(
            url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
            params= {
                'username': username, 
                'password': password
            }
        )
        output = '''
            ===================================
            Authentication test - Date {date}
            ===================================
            request done at "/permissions"
            | username={username}
            | password={password}
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
        print(output.format(date =datetime.now(), status_code=status_code, test_status=test_status, username = username, password=password))
        test_output = output.format(date = datetime.now(), status_code=status_code, test_status=test_status, username = username, password=password)

    except:
        print( 'Could not reach server')
        status_code = -1 
        test_output = "ERROR: Could not reach server" 
    

    # printing in a file
    print(os.environ.get('LOG'))
    if os.environ.get('LOG') == '1':
        print("Writing to a log file ")
        with open('/home/log_folder/api_test.log', 'a') as file:
            file.write(test_output)
    
    return status_code


if __name__ == "__main__":
    print("RUNNING TEST")
    try: 
        print("in block")
        authentication_check( api_address, api_port, 'alice', 'wonderland')
        print('SUCCESS')
    except:
       print("could not reach server")
    

    