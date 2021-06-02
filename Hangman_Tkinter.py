from tkinter import *
import random

#prints out defeat message
def endgame():
    lives_label1.destroy()
    lives_label.destroy()
    message_label1.destroy()
    hangman_label.destroy()
    hangman_label2.destroy()
    prompt_label.destroy()
    label1.destroy()
    label2.destroy()

    guess_label.configure(text = "The word was :" )
    message_label.configure(text="Hangman!!!",fg = "RED")
    word_label.configure(text = wrd)
    introlabel.configure(text = "Sorry...You Lost :(\tBetter Luck Next Time",font = (font,25),fg = secondary_color)
    logo_label.configure(text=hangman[0], font=('arial', 30))

#prints out victory message
def victory():
    input1.destroy()
    bt2.destroy()
    lives_label1.destroy()
    lives_label.destroy()
    message_label1.destroy()
    hangman_label.destroy()
    hangman_label2.destroy()
    prompt_label.destroy()
    label1.destroy()
    label2.destroy()

    guess_label.configure(text="The word was :")
    message_label.configure(text = "Good Job!! :)")
    word_label.configure(text=wrd)
    introlabel.configure(text="Congratulations You Guessed the Word Correctly!!\n\tVictoryy!!",font = (font,25))

#Checks if the guessed word is correct
def check_guess(guess):
    if guess not in wrd:#Incoorect guess
        message_label1.configure(text="Oh no!,Incorrect Guess",fg = "RED")
        lives[0] = lives[0] - 1
        if lives[0] == 0:
            input1.destroy()
            bt2.destroy()
            message_label.configure(text="Hangman!!!")
            hangman_label2.configure(text=hangman[0])
            endgame()
        else:
            process()

    else:
        for index in hdn_index:
            if guess == wrd[index]:
                hdn_wrd[index] = guess
                hdn_index.remove(index)      #Updates the hidden index by removing correctly guessed letters' index
                #print(hdn_index)
                if len(hdn_index) == 0:
                    bt2.destroy()
                    victory()
                else:
                    #print("Congratulations You Guessed Correctly!!", len(hdn_index), " more letters to go!!")
                    message_label1.configure(text="Congratulations You Guessed Correctly!!",fg = "GREEN",font = 30)
                    label1.configure(text = len(hdn_index) )
                    label2.configure(text = " more letters to go!!")
                    process()

#the input is converted to a string variable and checked if correct
def guess_word():
    guess = mystring.get()
    input1.delete(0, END)
    #print(guess)
    guess = guess.upper()
    if guess == wrd:
        victory()
    elif len(guess) == 1:
        check_guess(guess)
    else:  # If user inputs more than 1 letters/characters re-calls the function
        message_label1.configure(text="No Cheating!!\nJust one letter!!")
        lives[0] = lives[0] - 1
        if lives[0] == 0:
            input1.destroy()
            bt2.destroy()
            message_label1.configure(text="Hangman!!!")
            hangman_label2.configure(text=hangman[0])
            endgame()
        else:
            process()

def gg(event):
    guess_word()

#Prompts the user to guess a letter of the
def get_input():
    prompt_label.place(x=80, y=400)
    input1.place(x=50, y=450)
    input1.focus_set()
    bt2.place(x=350, y=450)
    bt2.configure(command= guess_word)
    root.bind("<Return>", gg)

#A fuction to hide the letters of the word
def hide_letters():
    for i in range(length):
        #randomly selects an index from the word and replaces it with "_"
        num = random.randint(0,length-1)
        if num not in hdn_index:
            hdn_index.append(num)

    for j in hdn_index:
        hdn_wrd[j] = "_"

#the loop that is repeated till lives left are 0
def process():
    # while lives[0] != 0:
    get_input()
    # print(hdn_index)
    update_word()
    #print(lives[0], "lives remaining")
    lives_label1.configure(text=lives[0])
    hangman_label2.configure(text=hangman[lives[0]])

#updates the hidden word as words are guessed
def update_word():
    guess_label.configure(text = "You have to guess the word : ",font = (font , 30),fg = secondary_color)
    word_label.configure(text = hdn_wrd , font = (font , 30), fg = tertiary_color)

#Initializes the game
def new_game():
    global lives, hdn_wrd, hide_letter, length, wrd, hdn_index, guess
    # declaring global variables
    bt1.destroy()
    # Provide a list to choose words from
    lst = ['Elephant', 'BlueWhale', 'Buffalo', 'Genda', 'Lmao']
    wrd = random.choice(lst).upper()  # Selects a random word from the list
    length = len(wrd)
    hdn_wrd = list(wrd)  # converts the word to a list to make it mutable
    # print(hdn_wrd)
    hidden_letter = []  # a list containing the hidden letters
    hdn_index = []  # A list containing the indices of the hidden letters in wrd


    logo_label.configure(text = "")
    word_label.configure(text = "")
    message_label.configure(text = "")
    introlabel.configure(text = "")
    lives_label.configure(text="Lives remaining :")
    lives_label.place(x=600, y=0)
    lives_label1.configure(text=lives[0])
    lives_label1.place(x=680, y=35)

    hangman_label.configure(text=" Hangman status :")
    hangman_label.place(x=600, y=100)
    hangman_label2.configure(text=hangman[lives[0]])
    hangman_label2.place(x=660, y=140)

    hide_letters()
    update_word()
    process()

#used when enter button is pressed, calls new game function
def ff(event):
    new_game()

#A list of different states of hangman. One is chosen depending on Lives remaining
hangman = [
"""   _
   |
   O
  /|\\
  / \\
""",
"""  _
  |
  O
 /|\\
 / 
""",
"""  _
  |
  O
 /|\\
 """,
"""  _
  |
  O
 /|""",
"""  _
  |
  O
  |""",
"""  _
  |
  O
""",
"""  _
  |
""",""" _ """," "]

root = Tk()                        #Opens tkinter window
root.geometry('800x800')           #dimensions of the window
root.configure(bg = 'white')
root.title("Hangman Game")
primary_color = "WHITE"
secondary_color = "DARK BLUE"
tertiary_color = "BLACK"
font = "Times New Roman"

lives = [8]  # Setting a fixed number of lives/chances the player has

#------------------------------------(All Labels)--------------------------------------
introlabel = Label(root,text = "Welcome to Hangman!!",font = (font,50),bg =primary_color)
introlabel.place(x = 100,y = 0)

guess_label = Label(root, font=(font, 30), fg=secondary_color)
guess_label.place(x = 0 , y = 150)

word_label = Label(root , font=(font, 30), bg=primary_color)
word_label.place(x = 100 , y = 220)

message_label = Label(root ,text = "Click Button to Start ",font=(font, 30), bg=primary_color)
message_label.place(x = 230 , y = 400)

message_label1 = Label(root ,font=(font, 30), fg= "Red",bg = primary_color)
message_label1.place(x = 230 , y = 550)

mystring = StringVar()
input1 = Entry(root, bg='WHITE', font=(35), fg='BLACK', relief='solid', justify='center', textvariable = mystring)

lives_label = Label(root ,font=(font, 18), fg=secondary_color)

lives_label1 = Label(root ,font=(font, 20), bg=primary_color)

logo_label = Label(root ,font=(font, 18),bg = primary_color, fg=secondary_color)
logo_label.configure(text = hangman[0],font = ('arial',30))
logo_label.place(x = 350,y = 100)

hangman_label = Label(root ,font=(font, 18), fg=tertiary_color)

hangman_label2 = Label(root ,font=(font, 22),fg=tertiary_color,bg=primary_color)

prompt_label = Label(root , font=(font, 24) )
prompt_label.configure(text = "Enter your guess : ")
input1 = Entry(root, bg='WHITE', font=(font , 20), fg='BLACK', relief='solid', justify='center', textvariable = mystring)

label1 = Label(root, font=(font, 15),bg = primary_color)
label1.place(x=50, y=300)
label2 = Label(root, font=(font, 15),bg = primary_color )
label2.place(x=70, y=300)

bt1 = Button(root,text = 'Start',font = (font, 30),bg = primary_color,fg = secondary_color,relief = "solid")
bt1.place(x = 330,y = 500)
bt1.configure(command = new_game )

bt2 = Button(root, text='Guess', font=(font, 30), bg=primary_color, fg=secondary_color, relief="solid")
root.bind("<Return>",ff)

#------------------------------------------------------------------------------------------------------
root.mainloop()