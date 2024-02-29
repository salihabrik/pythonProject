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

#for letter in secret_word:
 #   if letter == guess:
  #      print("Right")
   # else:
    #    print("Wrong")
    
game_over = false

while not game_over:
    
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word))