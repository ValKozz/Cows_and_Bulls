import random
from collections import Counter
from gamemath import GameMath


class AIGame(GameMath):
    '''AI in the old school game sense'''

    def __init__(self):
        super().__init__()
        self.possible_list = self.generate_new()

        self.node = self.possible_list.pop()
        self.bulls = 0
        self.cows = 0
        self.tries = 0

    def display(self):
        print(f'\nMy best guess is: {self.node}')
        self.take_input()

    def take_input(self):
        cow_input = input('Enter cows: ')
        bull_input = input('Enter Bulls: ')
        try:
            new_cows = int(cow_input)
            new_bulls = int(bull_input)
        except ValueError:
            print('Invalid input!')
            return self.take_input()

        if new_cows < 5 and new_bulls < 5:
            self.cows, self.bulls = int(cow_input), int(bull_input)
            return
        else:
            print('Invalid input!')
            return self.take_input()

    def generate_new(self):
        self.possible_list = []
        for i in range(123, 9877):
            str_i = str(i)

            if len(str_i) == 3:
                str_i = "0" + str_i
            # Use counter after zero append
            counter = Counter(str_i)

            if not any(value > 1 for value in counter.values()):
                self.possible_list.append(str_i)

        return self.possible_list

    def keep(self, guess, bulls, cows):
        clean_list = []

        for item in self.possible_list:
            new_cows, new_bulls = self.cow_or_bull(answer=guess, guess=item, to_display=False)

            if new_cows == cows and new_bulls == bulls:
                clean_list.append(item)
        self.possible_list = clean_list
        return self.possible_list

    def make_pick(self):
        try:
            self.node = random.choice(self.possible_list)
        except IndexError:
            print('Maybe you made a mistake? Conflicting results, no possible numbers left in sequence.')
        self.possible_list.remove(self.node)

    def game(self):
        while self.bulls < 4:
            self.tries += 1
            self.display()

            if self.bulls < 4:
                self.keep(self.node, self.bulls, self.cows)
                self.make_pick()

        print(f'My last guess is: {self.node}')
        print(f'Succeeded in {self.tries} tries.')

    def test_game(self, answer):
        while self.bulls != 4:
            self.tries += 1
            self.cows, self.bulls = self.cow_or_bull(answer=answer, guess=self.node, to_display=False)
            if self.bulls != 4:
                self.keep(self.node, self.bulls, self.cows)
                self.make_pick()
        if self.bulls == 4:
            return self.node, self.tries, self.possible_list
