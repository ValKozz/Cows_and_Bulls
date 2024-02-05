import random


class GameMath:
    def __init__(self):
        self.cows = 0
        self.bulls = 0

    def generate_array(self):
        str_array = ''
        while len(str_array) < 4:
            random_num = str(random.randint(0, 9))
            if random_num not in str_array:
                str_array += random_num
        return str_array

    def cow_or_bull(self, guess, answer, to_display=True):
        self.bulls = 0
        self.cows = 0
        for i in range(4):
            if guess[i] == answer[i]:
                self.bulls += 1
            elif guess[i] in answer and guess[i] != answer[i]:
                self.cows += 1
        if to_display:
            print(f'Cows: {self.cows}    Bulls: {self.bulls}')
        score = (self.cows, self.bulls)
        return score
