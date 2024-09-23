import requests 
import os
import json
import ast 
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
def search_google(data):
    
    """
    This is is supposed to gather additional information search by the users but not in the database/additional info
    
    """
    # link: str = 'google.com'
    api_key ='AIzaSyDziBZTAorR-d9AuiFumRFikyfT0dUlsA8'or os.getenv('GOOGLE_API') 
    search_engine_api = '73d6ddb13c5b5400e'or os.getenv('SEARCH_ENGINE')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': str(data),
        'key': api_key,
        'cx': search_engine_api
    }
    response = requests.get(url, params=params)
    print('type', ast.literal_eval(response.text))
    result = response.json()['items']
    return response.text
    # print(result)


def research(content):
    """
    This is supposed to gather additional information search by the users but not in the database/additional info
    """
    req = requests.get(link + content)



def search_gemini(data):
 
    import os
    import google.generativeai as genai

    genai.configure(api_key=os.environ["AIzaSyC2Au4SiCDJVpOgtXT5BcptrSoIOpFUqtc"])

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    {
    "role": "user",
    "parts": [
    "how many flags of philippines iteration are there\n",
    ],
    },
    {
    "role": "model",
    "parts": [
    "There have been **four** official iterations of the Philippine flag throughout its history:\n\n1. **First Republic Flag (1898-1901)**: This was the first national flag, with a **blue triangle** at the hoist, a **red triangle** at the fly, and a **white equilateral triangle** in the center. The sun with eight rays and three stars were in the center white triangle. \n2. **Malolos Constitution Flag (1899)**: This flag was similar to the First Republic Flag, but it had **eight rays** on the sun instead of the original **eight points**.\n3. **Commonwealth Flag (1936-1946)**: This flag is the same as the First Republic Flag, with the **sun having eight rays**.\n4. **Present Flag (1946-present)**:  This is the current flag, also the same as the First Republic Flag and the Commonwealth Flag, with the **sun having eight rays**.\n\nWhile there have been four official iterations, the **most important distinction is between the original First Republic Flag with eight points on the sun and the subsequent versions with eight rays**.  This difference was rectified when the Commonwealth flag adopted the eight rays in 1936. \n",
    ],
    },
    ]
    )

    response = chat_session.send_message(data)

    return response.text