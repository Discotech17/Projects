# edureka.co hangman tutorial
import random

name = input('Please enter your name: ')
print('Hello,' + name, 'Let\'s play hangman.')

wordList = ['apple', 'butterfly', 'motorcycle', 'potato', 'vodka', 'delicious', 'zebra',\
            'puppy', 'giraffe', 'python', 'spine', 'track', 'hilarious', 'spontaneous',\
            'generator']

word = random.choice(wordList)

print(len(word))

turns = 10

guesses = ''

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print('You won')
        break

    print()
    guess = input('Guess a letter: ')

    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong guess')
        print('You have', + turns, 'more guesses left')

        if turns == 0:
            print('You lose!')
