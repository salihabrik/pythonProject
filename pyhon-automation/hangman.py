import random

print ("Welcome to Hangman Game")
words = ['hacker', 'bounty', 'random']

secret_word = random.choice(words)
print ("secret_word")
print("you get 5 guesses")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)    
#guess = input("Guess a letter ").lower()

#print(guess)

#for letter in secret_word:
 #   if letter == guess:
  #      print("Right")
   # else:
    #    print("Wrong")
num = 0   
game_over = False

while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
        if guess not in secret_word:
            num += 1
            guesses_left = 5 - num
            print(f" you have {guesses_left} guesses left ")
            if num >= 5:
                print("you loser") 
                game_over = True
    print(display_word)
    
    if "_" not in display_word:
        print("you win")
        game_over = True