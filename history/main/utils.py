# import google.generativeai as genai

# genai.configure(api_key="AIzaSyBr9V_Mb4NovM4bIDftgVdD3qkz-6q1S0Q")

# # Set up the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 0,
#   "max_output_tokens": 8192,
# }

# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]

# model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)

# convo = model.start_chat(history=[
#   {
#     "role": "user",
#     "parts": ["theory of jose rizal being jack the reaper"]
#   },
#   {
#     "role": "model",
#     "parts": ["## José Rizal as Jack the Ripper: Exploring the Theory\n\nThe idea of José Rizal, the Philippine national hero, being Jack the Ripper, the infamous unidentified serial killer who terrorized London in 1888, is a fringe theory that has circulated online and in some niche communities. It's important to note that there's **no credible historical evidence** to support this claim, and it's widely considered to be a **conspiracy theory**.\n\n### Arguments Presented for the Theory:\n\n* **Timeline Overlap:** Rizal was in London during the time of the Ripper murders, studying medicine and writing. \n* **Surgical Skills:** As a medical student, Rizal had anatomical knowledge and surgical skills, which some argue could be consistent with the Ripper's methods.\n* **Anti-Colonial Sentiment:**  The theory suggests that Rizal, fueled by anger towards colonial powers, targeted victims who represented symbols of British imperialism.\n\n### Counterarguments and Issues:\n\n* **Lack of Evidence:** There is no historical record or document linking Rizal to the murders. His known activities and writings during his time in London do not suggest any involvement in such crimes.\n* **Character and Values:** Rizal was known for his peaceful and intellectual nature, advocating for reform through his writings rather than violence. Connecting him to brutal murders contradicts his established character.\n* **Profile Discrepancy:** The psychological profile often associated with Jack the Ripper doesn't align with Rizal's known personality and background.\n\n### Origins and Spread of the Theory:\n\nThe origin of this theory is unclear, but it seems to have emerged and gained traction online, particularly within Filipino online communities. Some suggest it could be a form of \"historical revisionism\" or a way to explore alternative narratives surrounding historical figures.\n\n### Conclusion:\n\nWhile the idea of José Rizal being Jack the Ripper might be intriguing to some, it's crucial to approach it with a critical and evidence-based perspective.  The available evidence overwhelmingly contradicts this theory, making it highly improbable.  \n\n**It's important to remember that José Rizal is a revered figure in Philippine history, recognized for his intellectual contributions and peaceful advocacy for reform. Associating him with such gruesome acts without credible evidence disrespects his legacy and historical significance.**"]
#   },
# ])

# convo.send_message("crazy philippines history theory")
# # print(convo.last.text)