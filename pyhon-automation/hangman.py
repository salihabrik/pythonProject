import random

print ("Welcome to Hangman Game")
words = ['hacker', 'bounty', 'random']

secret_word = random.choice(words)

display_word = []
for letter in secret_word:
    display_word += "_"
    print(display_word)
    
    
guess = input("Guess a letter ").lower()

#print(guess)

for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")