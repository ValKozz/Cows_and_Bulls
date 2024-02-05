import time
from ai_player import AIGame
from collections import Counter


def count():
    with open('test.txt', 'r+') as file:
        file.writelines('\n')
        file.writelines('\n\nWrongs:\n')
        wrong = 0
        for line in file.readlines():
            try:
                answer = line.split('Answer')[1][1:6].strip()
                guess = line.split('Guess')[1][2:6].strip()
                if answer != guess:
                    wrong += 1
                    file.writelines(line)
            except IndexError:
                pass

        if wrong:
            failure_rate = (wrong / 5040) * 100
            print(f'Failre rate: {"{:.2f}".format(failure_rate)}%')
            file.writelines(f'Total wrongs: {wrong}\n')
            file.writelines(f'Failre rate: {"{:.2f}".format(failure_rate)}%')

        else:
            print(f'No mistakes detected!')
            file.writelines(f'No mistakes detected!')


def run_test():
    number_list = []

    for i in range(123, 9877):
        str_i = str(i)

        if len(str_i) == 3:
            str_i = "0" + str_i
        # Use counter after zero append
        counter = Counter(str_i)

        if not any(value > 1 for value in counter.values()):
            number_list.append(str_i)

    guess_number = 0

    with open('test.txt', 'w') as file:
        start_time_whole = time.time()
        for number in number_list:
            guess_number += 1
            print(f'Attempt {guess_number}')
            ai_game = AIGame()

            start = time.time()
            answer = ai_game.test_game(answer=number)
            end_time = time.time()
            result = end_time - start

            file.writelines(
                f'{guess_number}. Answer: {number}, Guess: {answer[0]}, Attempts: {answer[1]}, Time: {("{:.4f}".format(result))}, Possible left: {answer[2]}\n')

        end_time_whole = time.time()
        time_in_minutes = (end_time_whole - start_time_whole) / 60
        file.writelines(f'Time elapsed for whole script: {("{:.2f}".format(time_in_minutes))} minutes.\n')
        count()
