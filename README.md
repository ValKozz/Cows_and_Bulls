# Cows and Bulls #

A version of the cows and bulls game.

https://en.wikipedia.org/wiki/Bulls_and_cows
# How it's played #
It involves 2 players. One thinks of a 4-digit number with no repeating digits and the opponent must guess what it is using hints.
The hints consist of a number of 'Cows' and 'Bulls'. Cows are correct digits in the wrong place and Bulls are correct digits in the right place.

    Answer: 1234
    Guess: 2039

    Cows: 1
    Bulls: 1

2 is a part of the correct number sequence, but it stands in index [1] or the second place instead of the first one as it is in the guess.

3 is in the right place and is a part of the correct sequence, so it's counted as a bull.


The game continues untill 4 bulls are found.

# Exmple games #
Python tries to guess. Secret number 9205:
    
    My best guess is: 9876
    Enter cows: 0
    Enter Bulls: 1
    
    My best guess is: 9140
    Enter cows: 1
    Enter Bulls: 1
    
    My best guess is: 9305
    Enter cows: 0
    Enter Bulls: 3
    
    My best guess is: 9205
    Enter cows: 0
    Enter Bulls: 4

    My last guess is: 9205
    Succeeded in 4 tries.


Player tries to guess generated number:
    
    Enter 4 digit number:
    1234
    Cows: 0    Bulls: 0

    Enter 4 digit number:
    5678
    Cows: 2    Bulls: 0

    Enter 4 digit number:
    7890
    Cows: 0    Bulls: 3

    Enter 4 digit number:
    5789
    Cows: 2    Bulls: 0

    Enter 4 digit number:
    7896
    Cows: 1    Bulls: 2

    Enter 4 digit number:
    7860
    Cows: 1    Bulls: 2

    Enter 4 digit number:
    6890
    Cows: 0    Bulls: 4
    Congrats, you won!
    Tries: 7


# Running tests #
A script to run tests with all possible combinations of numbers is included 
for anyone who wishes to see if the algorithm will make any mistakes.
Just type test when asked for mode selection input. This will create a tests.txt file
containing results and mistakes, including time it took to run each combo of numbers.