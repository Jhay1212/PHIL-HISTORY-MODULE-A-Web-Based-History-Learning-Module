import requests 
import os
link: str = 'google.com'
api_key = os.getenv('GOOGLE_API')
search_engine_api = os.getenv('SEARCH_ENGINE')
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'query': 'hello',
    'key': api_key,
    'cx': search_engine_api
}
response = requests.get(url, params=params)
print(response)
def search_google():
    
    """
    This is is supposed to gather additional information search by the users but not in the database/additional info
    
    """
    # link: str = 'google.com'
    api_key ='AIzaSyDziBZTAorR-d9AuiFumRFikyfT0dUlsA8'or os.getenv('GOOGLE_API') 
    search_engine_api = '73d6ddb13c5b5400e'or os.getenv('SEARCH_ENGINE')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': 'hello',
        'key': api_key,
        'cx': search_engine_api
    }
    response = requests.get(url, params=params)
    print(response.text)
    result = response.json()['items']
    # print(result)


def research(content):
    """
    This is supposed to gather additional information search by the users but not in the database/additional info
    """
    req = requests.get(link + content)