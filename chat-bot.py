from difflib import get_close_matches
from datetime import datetime


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: >>')

        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Chatbot: {answer}')
        else:
            print("Chatbot: I can't understand...")


if __name__ == '__main__':
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    brain: dict = {'hello': 'hey there!', 'how are you': 'i am good , thanks', 'what is your name': 'I am a chatbot',
                   'what time is it?': f'"Current Time =", {current_time}',
                   'what can you do ? ': 'i can answer the questions', 'thank you': 'your welcome'}

    chat_bot(knowledge=brain)
