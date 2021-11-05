from flask import Flask , render_template, url_for, redirect, request
import random
from lists import lst, hangman

app = Flask(__name__)


@app.route('/', methods = ['POST','GET'])
def reset():
    global score
    score = 0
    new_game()
    return render_template('hangman.html', lives=lives, hdn_wrd=hdn_wrd, hangman=hangman[lives], hdn_index=hdn_index)


@app.route('/gameover/finalscore',methods = ['POST','GET'])
def thankyou():
    global score
    return render_template("endgame.html",score = score)

@app.route('/newgame',methods = ['POST','GET'])
def play_again():
    new_game()
    return render_template('hangman.html',lives = lives , hdn_wrd = hdn_wrd , hangman = hangman[lives],hdn_index = hdn_index)


@app.route('/gameover',methods = ['POST','GET'])
def endgame():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,shn_index,message,score
    return render_template("gameover.html",score = score, wrd = wrd)


@app.route('/victory',methods = ['POST','GET'])
def victory():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index, shn_index,message,score
    score += 1
    return render_template("victory.html", score = score, wrd = wrd)


def check_guess(guess):
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index, shn_index, message, flag
    # Incorrect guess
    if guess not in wrd:
        lives = lives - 1
        message = "Uh Oh !Incorrect Guess :( Try again !!"
        flag = 0
    else:
        for index in hdn_index:
            if guess == wrd[index]:
                hdn_wrd[index] = guess
                hdn_index.remove(index)
                message = "You Guessed Correctly !! " + str(len(hdn_index))  + "more letters to go"
                flag = 1
                break
    return message,flag


@app.route('/guess',methods = ['POST','GET'])
def guess_word():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,shn_index,message
    guess = request.form['guess']
    guess = guess.upper()
    if guess == wrd:
        return victory()
    elif len(guess) > 1:
        lives -= 1
        message = "Only one letter allowed"
    elif len(guess) == 1:
        message = check_guess(guess)
        if len(hdn_index) == 0:
            return victory()
        elif lives == 0:
            return endgame()
    return render_template('message.html', lives=lives, hdn_wrd=hdn_wrd, hangman=hangman[lives],hdn_index = hdn_index,message = message)


@app.route('/',methods = ['POST','GET'])
def update_word():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,shn_index,message
    if lives > 0:
        return render_template('hangman.html',lives = lives , hdn_wrd = hdn_wrd , hangman = hangman[lives],hdn_index = hdn_index)
    else:
        return endgame()


def hide_letters():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,shn_index,message
    if len(wrd) > 6:
        for i in range(2):
            num = random.randint(0,length)
            shn_index.append(num)
    for i in range(length):
        if i not in shn_index:
            hdn_wrd[i] = '_'
            hdn_index.append(i)
        else:
            hdn_wrd[i] = wrd[i]


def new_game():
    global lives, hdn_wrd, hidden_letter, length, wrd, hdn_index,shn_index,message
    wrd = random.choice(lst).upper()
    length = len(wrd)
    hdn_wrd = list(wrd)
    hidden_letter = []
    hdn_index = []
    shn_index = []
    lives = 7
    hide_letters()


score = 0
new_game()
if __name__ == '__main__':
    app.run(debug=True)
