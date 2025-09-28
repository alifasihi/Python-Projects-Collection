import random
import sys


class RPS:
    def __init__(self):
        print('Welcome to  RPS!')

        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valis_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('rock , paper or scissors? >>').lower()

        if user_move == 'exit'.lower():
            print('tanks for playing...')
            sys.exit()

        if user_move not in self.valis_moves:
            print('Invalid moves...')
            return self.play_game()

        ai_move: str = random.choice(self.valis_moves)
        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_move(self, user_move: str, ai_move: str):
        print('============')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('============')

    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('it is a tie....')
        elif user_move == 'rock'.lower() and ai_move == 'scissors'.lower():
            print('You Win...')
        elif user_move == 'scissors'.lower() and ai_move == 'paper'.lower():
            print('You Win...')
        elif user_move == 'paper'.lower() and ai_move == 'rock'.lower():
            print("You Win...")
        else:
            print('AI Win!')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
