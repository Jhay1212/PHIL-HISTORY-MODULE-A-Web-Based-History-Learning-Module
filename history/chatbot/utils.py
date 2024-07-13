import json 
from difflib import get_close_matches

def load_data(filename: str) -> dict:
    with open(filename, 'r') as file:
        data = file.read()

    return data

def save_data(data: dict, filename: str)  -> None:
    with open(filename, 'w') as file:
        json.dumps(data, filename, indent=4)

    

def find_save_matches(user_question: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=.8)
    return matches if matches else None

def get_answer_for_question(question: str, data_pool: dict) -> str:
    for q in data_pool['questions']:
        if q['question'] == question:
            return q['answer']
        

def chatbot():
    knowledge_base = load_data('data.json')
    question = input('Enter a question: ').lower()

    best_match = find_save_matches(question=question, data_pool=[q['question'] for q in knowledge_base['questions']])
    if best_match:
        print(best_match)
    else:
        None


if __name__ == '__main__':
    chatbot()