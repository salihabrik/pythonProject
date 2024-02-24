import random

print ("Welcome to Hangman Game")
words = ['hacker', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']

secret_word = random.choice(words)

guess = input("Guess a letter").lower()

print(guess)

for letter in secret_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")