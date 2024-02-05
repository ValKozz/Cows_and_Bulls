from ai_player import AIGame
from gamemath import GameMath
from run_tests import run_test


class Game(GameMath):
    def __init__(self):
        super().__init__()
        self.answer = ''
        self.guess = ''
        self.tries = 0

    def clean_input(self):
        input_ = input('Enter 4 digit number:\n')

        if not input_.isnumeric():
            print('Only numeric values allowed!')
            return self.clean_input()

        if len(set(input_)) != 4:
            print("No duplicates allowed!")
            return self.clean_input()

        self.guess = input_

    def check_player_answer(self):
        self.clean_input()
        self.cow_or_bull(self.guess, self.answer)
        self.tries += 1

    def player_game(self):
        self.answer = self.generate_array()
        while self.answer != self.guess:
            self.check_player_answer()
        print('Congrats, you won!')
        print(f'Tries: {self.tries}')

    def ai_game(self):
        ai_player = AIGame()
        ai_player.game()


if __name__ == '__main__':
    game = Game()

    print('''Cow and Bull by Valeri Kozarev - @ValKozz.
    The game is played by making up a secret number, consisting of four different digits. The opponent must in return
    guess them. If the guess contains a number that is present in the answer, the opposing player must say if it's either a 
    bull or a cow. Cows are numbers in the wrong place and Bulls, numbers in the proper position.
    c - The computer tries to guess your number.
    p - You try and guess the number the computer has generated.
    test - Run tests, will create a tests.txt file in the directory of the game.''')

    def ask_player():
        mode = input('Player or CPU guesses? (p/c)\n').lower()
        if mode == 'p':
            game.player_game()
        elif mode == 'c':
            game.ai_game()
        elif mode == 'test':
            run_test()
        else:
            print('Invalid input.')
            return ask_player()
    ask_player()

