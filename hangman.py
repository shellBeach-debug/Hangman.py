import random

guessed = []
word_show = []
guess = ""
listed_word = []
word_of_round = ""


#function where the actual game happens
def guess():
    
    guessed = [] #resets the guess counter

    #opens the wordlist and picks a word
    def select_word():
        file = open("wordlist.txt", "r")
        content = file.readlines()
        file.close()
        x = random.randint(0, 995)
        word = content[x]
        return word[:-1] #returns the word excluding the last character, which is not needed

    word_of_round = select_word()
    listed_word = list(word_of_round)


    #shows the current situation with the guessed letters and word composition and if all the guessed letters equal word_of_round then returns True to indicate that all the letters have been found
    def print_situation():
        x = 0
        a = ''

        for i in word_of_round: #updating the variable for the word of the current game, that is displayed and partially covered with *
            if char_word == i:
                listed_word.insert(x, i)
            elif i in guessed:
                listed_word.insert(x, i)
            else:
                listed_word.insert(x, '*')
            a += listed_word[x]       
            x += x
        print(a)
        if a == word_of_round:
            return True #if all the letters of the word have been found, then True is returned

    #function for winning the game 
    def win():
        print("\033[H\033[2J", end="") #clear screen
        print("Hurraah, you have successfully avoided the hanging!\n\n\n")
        print(f"The correct word is: {word_of_round}\n\n\n")
        input("Press enter to continue...")

    #checks if the maximum number of guesses has been reached and returns True if GAME OVER
    def guess_counter(y): 
        turns = len(word_of_round)
        if turns - y == 0:
            print(f"Guess limit reached\n\nWord of the round was: {word_of_round}\n\n\nGAME OVER")
            input("\n\n\nPress enter to continue...")
            return True
    
    #checking if the guessed word is the right word
    def word_check(word):
        if word == word_of_round:
            win()
            return True
        else:
            print("Sorry, that is not the correct word.\n\n\n")
            input("Press enter to continue...")

    #gameloop
    while True:
        char_word = input("Guess a letter by entering one letter, or try to guess the word by typing 'guess'.\n>")

        if char_word == 'guess': 
            print("\033[H\033[2J", end="") #ANSI escape code to clear screen
            guess = input("\n\n\nGuess the word and press enter.\n>")      
            if word_check(guess) == True:
                break
            y = len(guessed) # guess counter
            z = len(word_of_round)
            print(f"Number of guesses: {y}/{z}")
            if guess_counter(y) == True:
                break
        
        if char_word in guessed and char_word != 'guess':
            print("\033[H\033[2J", end="")
            print("You already have tried to guess that letter!\n\n\n")
            print_situation()
            y = len(guessed)
            z = len(word_of_round)
            print(f"Number of guesses: {y}/{z}")
            if guess_counter(y) == True:
                break

        elif char_word in word_of_round and char_word not in guessed and char_word != 'guess':
            print("\033[H\033[2J", end="")
            print(f"Letter \'{char_word}\' is part of the word!\n\n\n")
            guessed.append(char_word)
            b = print_situation()
            if b == True:
                win()
                break
            y = len(guessed)
            z = len(word_of_round)
            print(f"Number of guesses: {y}/{z}")
            if guess_counter(y) == True:
                break

        elif char_word != 'guess':
            print("\033[H\033[2J", end="")
            print(f"Letter \'{char_word}\' is not part of the word\n\n\n")
            guessed.append(char_word)
            print_situation()
            y = len(guessed)
            z = len(word_of_round)
            print(f"Number of guesses: {y}/{z}")
            if guess_counter(y) == True:
                break

#game lobby loop
def start():   
    while True:
        print("\033[H\033[2J", end="")
        choice = input("If you want to play a game of Hangman, press P and hit enter.\n\nIf you want to quit press Q and hit enter.\n\n")
        if choice == 'p' or choice == 'P':
            print("\033[H\033[2J", end="")
            guess()
        if choice == 'q' or choice == 'Q':
            print("It was fun, have a nice day!")
            break


start()
