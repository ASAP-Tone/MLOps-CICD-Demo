import os
import requests
from datetime import datetime
# definition of the API address
api_address = '0.0.0.0'
# API port
api_port = 8000
# requête
import time


def content_check( api_address : str, port : int , version : str, username : str, password : str, sentence : str ) -> str: 
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
            ============================
            Content Test - Date {date}
            ============================
            request done at "{version}/sentiment"
            | username={username}
            | password={password}
            | sentence={sentence}
            actual restult = {api_sentiment}
            ==>  {test_status}
            '''
            # query status
        response_body = r.json()
        sentiment_score = response_body["score"]
        # display the results
        if sentiment_score > 0:  # and sentiment == 'positive':
            test_status = 'positive'
        # if sentiment_score <= 0 #and sentiment == 'negative':
        #     test_status = 'passed'
        else:
            test_status = 'negative'
        print(output.format(date=datetime.now(), api_sentiment = sentiment_score,  version=version,  
                            username = username, password=password, sentence=sentence, test_status = test_status))
        
        test_output = output.format(date=datetime.now(), api_sentiment = sentiment_score,  version=version,  
                            username = username, password=password, sentence=sentence, test_status = test_status)
    except:
        print( 'Could not reach server')
        status_code = -1 
        test_output = "ERROR: Could not reach server" 
        return test_output
    
    # printing in a file
    if os.environ.get('LOG') == '1':
        with open('/home/log_folder/api_test.log', 'a') as file:
            file.write(test_output)
    
    return test_status


# if __name__ == "__main__":

#     test_permissions( api_address, api_port, 'alice', 'wonderland')
#     test_permissions( api_address, api_port, 'bob', 'builder')
#     test_permissions( api_address, api_port, 'tony', 'ruiz')



    