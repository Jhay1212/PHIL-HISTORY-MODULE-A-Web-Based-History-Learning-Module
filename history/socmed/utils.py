import os

import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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
        "how did rizal get captured\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "José Rizal wasn't captured in the traditional sense of being caught red-handed or after a chase. His apprehension was a result of a complex interplay of factors and events:\n\n**1. Exile to Dapitan:** After publishing his novels *Noli Me Tangere* and *El Filibusterismo*, Rizal's writings, deemed subversive by the Spanish authorities, made him a target. In 1892, he was exiled to Dapitan, Mindanao. While seemingly isolated, Rizal remained active, writing, teaching, and corresponding with nationalist groups. This kept him on the authorities' radar.\n\n**2. The Katipunan and the Cry of Balintawak:** In 1896, Andres Bonifacio and the Katipunan, a secret society advocating Philippine independence, initiated an armed revolution against Spain.  Though Rizal consistently advocated for peaceful reforms, the Spanish authorities saw the Katipunan's uprising as an opportunity to eliminate him, viewing him as the symbolic leader and inspiration behind the rebellion.\n\n**3. Arrest and Imprisonment:** In July 1896, Rizal was granted permission to travel to Cuba as a volunteer doctor. However, while en route aboard a Spanish ship, he was arrested upon reaching Barcelona.  The outbreak of the revolution provided a convenient pretext for his detention. He was shipped back to the Philippines as a prisoner and imprisoned in Fort Santiago.\n\n**4. Trial and Execution:**  Despite a lack of concrete evidence directly linking him to the Katipunan's armed struggle, Rizal was subjected to a hasty trial by a Spanish military court. He was falsely accused of rebellion, sedition, and conspiracy. On December 30, 1896, Rizal was executed by firing squad in Manila at the age of 35.\n\n**Key Takeaway:** While not captured in a traditional sense, Rizal's apprehension and execution resulted from his writings' impact, the Spanish authorities' paranoia, and their desire to crush the growing Philippine revolution by silencing its perceived ideological leader.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "in flask how do i get additional info that is not in my data base ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here's a breakdown of how to handle getting information beyond your Flask database in your web application, along with best practices and examples:\n\n**Key Concepts**\n\n* **Flask's Core:** Flask is a web framework, providing the structure for routing requests and sending responses. It relies on other libraries for data management.\n* **Databases:** Your database (e.g., SQLite, PostgreSQL, MySQL) stores core data. It's great for user accounts, products, etc.\n* **External APIs:** Many services (like weather, maps, financial data) provide APIs to access their information.\n* **Data Retrieval:** You'll use libraries like `requests` (for making API calls) and potentially a data parsing library like `json` or `xml` to handle the responses.\n\n**Methods to Get Additional Info**\n\n1. **External APIs:**\n\n   * **Example: Weather Forecast**\n      ```python\n      import requests\n\n      @app.route('/weather/<city>')\n      def get_weather(city):\n          api_key = 'your_api_key'  # Get from a weather API provider\n          base_url = 'http://api.openweathermap.org/data/2.5/weather?'\n          complete_url = base_url + 'appid=' + api_key + '&q=' + city\n\n          response = requests.get(complete_url)\n          data = response.json()\n\n          # Extract and display weather information\n          if data['cod'] != '404': \n              temperature = data['main']['temp']\n              description = data['weather'][0]['description']\n              return f\"The weather in {city} is {description} with a temperature of {temperature} Kelvin.\"\n          else:\n              return 'City not found.'\n      ```\n\n2. **Web Scraping (Use with Caution):**\n\n   * **Example: Extracting Product Prices**\n      ```python\n      from bs4 import BeautifulSoup\n      import requests\n\n      @app.route('/product/<product_name>')\n      def get_product_price(product_name):\n          url = 'https://www.example.com/search?q=' + product_name  # Replace with the target website\n          response = requests.get(url)\n          soup = BeautifulSoup(response.content, 'html.parser')\n\n          # Find the price element (adjust selectors as needed)\n          price_element = soup.find('span', class_='product-price')\n          if price_element:\n              price = price_element.text.strip()\n              return f\"The price of {product_name} is {price}.\"\n          else:\n              return 'Price not found.'\n      ```\n\n**Important Considerations**\n\n* **API Keys:**  Securely store your API keys. Don't commit them directly into your code. Use environment variables or configuration files.\n* **API Rate Limits:** APIs often have usage limits. Respect them to avoid getting blocked.\n* **Data Parsing:**  API responses often come in JSON or XML formats. You'll need to use libraries to parse them into Python data structures.\n* **Scraping Responsibility:**  Be mindful of website terms of service when scraping. Use a polite scraping agent (avoid overloading websites).\n* **Caching:**  Store frequently accessed data in a cache (e.g., Redis) to reduce API calls and improve performance.\n\n**Example Flask Application Structure**\n\n```python\nfrom flask import Flask, render_template\n\napp = Flask(__name__)\n\n# ... Your database setup (e.g., SQLAlchemy) ...\n\n@app.route('/')\ndef index():\n    # Fetch data from your database\n    db_data = get_data_from_database()\n\n    # Get additional information from an external API\n    api_data = get_weather_from_api('New York') \n\n    return render_template('index.html', db_data=db_data, api_data=api_data)\n\n# ... Your database functions ...\n# ... API functions ...\n\nif __name__ == '__main__':\n    app.run(debug=True)\n```\n\n**Key Points**\n\n* **Database:** Use your database for the core data that your application manages.\n* **External APIs:**  Use APIs for data that is constantly updated or too complex to store in your database.\n* **Data Parsing:**  Learn how to handle and process data from different formats (JSON, XML).\n* **Efficiency:** Optimize your data retrieval (caching) for better user experiences.\n\nLet me know if you'd like more specific examples or guidance on using a particular API! \n",
      ],
    },
  ]
)


def send_message(message):
    response = chat_session.send_message(message)
    return response.text




# import google.generativeai as genai

# genai.configure(api_key="AIzaSyBr9V_Mb4NovM4bIDftgVdD3qkz-6q1S0Q")

# # Set up the model
# generation_config = {
# "temperature": 1,
# "top_p": 0.95,
# "top_k": 0,
# "max_output_tokens": 8192,
# }

# safety_settings = [
# {
# "category": "HARM_CATEGORY_HARASSMENT",
# "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# },
# {
# "category": "HARM_CATEGORY_HATE_SPEECH",
# "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# },
# {
# "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# },
# {
# "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# },
# ]

# model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
#                             generation_config=generation_config,
#                             safety_settings=safety_settings)

# convo = model.start_chat(history=[
# {
# "role": "user",
# "parts": ["theory of jose rizal being jack the reaper"]
# },
# {
# "role": "model",
# "parts": ["## José Rizal as Jack the Ripper: Exploring the Theory\n\nThe idea of José Rizal, the Philippine national hero, being Jack the Ripper, the infamous unidentified serial killer who terrorized London in 1888, is a fringe theory that has circulated online and in some niche communities. It's important to note that there's **no credible historical evidence** to support this claim, and it's widely considered to be a **conspiracy theory**.\n\n### Arguments Presented for the Theory:\n\n* **Timeline Overlap:** Rizal was in London during the time of the Ripper murders, studying medicine and writing. \n* **Surgical Skills:** As a medical student, Rizal had anatomical knowledge and surgical skills, which some argue could be consistent with the Ripper's methods.\n* **Anti-Colonial Sentiment:**  The theory suggests that Rizal, fueled by anger towards colonial powers, targeted victims who represented symbols of British imperialism.\n\n### Counterarguments and Issues:\n\n* **Lack of Evidence:** There is no historical record or document linking Rizal to the murders. His known activities and writings during his time in London do not suggest any involvement in such crimes.\n* **Character and Values:** Rizal was known for his peaceful and intellectual nature, advocating for reform through his writings rather than violence. Connecting him to brutal murders contradicts his established character.\n* **Profile Discrepancy:** The psychological profile often associated with Jack the Ripper doesn't align with Rizal's known personality and background.\n\n### Origins and Spread of the Theory:\n\nThe origin of this theory is unclear, but it seems to have emerged and gained traction online, particularly within Filipino online communities. Some suggest it could be a form of \"historical revisionism\" or a way to explore alternative narratives surrounding historical figures.\n\n### Conclusion:\n\nWhile the idea of José Rizal being Jack the Ripper might be intriguing to some, it's crucial to approach it with a critical and evidence-based perspective.  The available evidence overwhelmingly contradicts this theory, making it highly improbable.  \n\n**It's important to remember that José Rizal is a revered figure in Philippine history, recognized for his intellectual contributions and peaceful advocacy for reform. Associating him with such gruesome acts without credible evidence disrespects his legacy and historical significance.**"]
# },
# ])

# convo.send_message("crazy philippines history theory")
# # print(convo.last.text)
