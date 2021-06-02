import random

#prints out defeat message
def endgame():
    print("The word was", wrd)
    print("\nSorry You Lost Better Luck Next Time")

    chc = input("\n\nDo you want to play again  Y\\N : ").upper()
    if chc =='y':
        new_game()
    else:
        quit()

#prints out victory message
def victory():
    print("The word was",wrd)
    print("Congratulations You Guessed the Word Correctly!!\nVictoryy!!")
    chc = input("\n\nDo you want to play again Y\\N : ").upper()
    if chc =='Y':
        new_game()
    else:
        quit()

#A fuction to hide the letters of the word
def hide_letters():
    for i in range(length):
        #randomly selects an index from the word and replaces it with "_"
        num = random.randint(0,length-1)
        if num not in hdn_index:
            hdn_index.append(num)

    for j in hdn_index:
        hdn_wrd[j] = "_"

# Prints out the updated hidden word
def update_word():
    print("Guess the word : ")
    for letter in hdn_wrd:
        print(letter, end=" ")
#        if letter != "_" :
#           gsd_letters.append(letter)
#    for letter in hdn_index:
#        ungsd_letters.append(wrd[letter])
    print()

#Checks if the guessed word is correct
def check_guess(guess):
    if guess not in wrd:#Incoorect guess
        print("Oh no!,Incorrect Guess")
        return "absent"

    else:
        for index in hdn_index:
            if guess == wrd[index]:
                hdn_wrd[index] = guess
                hdn_index.remove(index)      #Updates the hidden index by removing correctly guessed letters' index
                #print(hdn_index)
                if guess in gsd_letters and guess not in ungsd_letters:
                    print("Already guessed that!")
                if len(hdn_index) == 0:
                    victory()
                else:
                    print("Congratulations You Guessed Correctly!!", len(hdn_index), " more letters to go!!")
                return "present"

#Prompts the user to guess a letter of the
def guess_word():
    guess = input("\nEnter your guess :")
    guess = guess.upper()
    if guess == wrd:
        victory()
    elif len(guess) == 1:
        stat = check_guess(guess)
        return stat
    else: #If user inputs more than 1 letters/characters re-calls the function
        print("No Cheating!!\nJust one letter!!")
        guess_word()


#A list of different states of hangman. One is chosen depending on Lives remaining
hangman = [
"""
  _
  |
  O
 /|\\
 / \\
""",
"""
  _
  |
  O
 /|\\
 / 

""","""
  _
  |
  O
 /|\\
 ""","""
  _
  |
  O
 /|""","""
  _
  |
  O
  |""",
"""
  _
  |
  O
""","""
  _
  |
""",""" _ """]

#Start a new game
def new_game():
    print("Welcome To Hangman !!")
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,gsd_letters,ungsd_letters #declaring global variables
    # Provide a list to choose words from
    lst = ['Elephant', 'BlueWhale', 'Buffalo', 'Genda', 'Lmao']
    gsd_letters = []
    ungsd_letters = []
    wrd = random.choice(lst).upper()  # Selects a random word from the list
    length = len(wrd)

    hdn_wrd = list(wrd)  # converts the word to a list to make it mutable
    # print(hdn_wrd)
    hidden_letter = []  # a list containing the hidden letters
    hdn_index = []  # A list containing the indices of the hidden letters in wrd

    lives = 8  # Setting a fixed number of lives/chances the player has

    hide_letters()
    #print(hdn_wrd)
    #print(hdn_index)
    update_word()
    while lives>0:
        check = guess_word()
        #print(hdn_index)
        update_word()
        if check == "present":
            continue
        elif check == "absent":
            lives = lives - 1
            print(lives,"lives remaining")
            print("Hangman status :")
            print(hangman[lives])
        else:
            continue

    if lives == 0:
        print("Hangman!!!")
        endgame()

new_game()   #Initializes the game