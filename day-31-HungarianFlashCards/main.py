from tkinter import *
import pandas
import random as rand

new_card = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data_frame = pandas.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data_frame = pandas.read_csv("./data/hungarian_words.csv")

data = data_frame.to_dict(orient="records")

#GENERATING RANDOM WORDS
def next_card():
    global timer, new_card
    window.after_cancel(timer)

    new_card = rand.choice(data)

    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title, text = "Hungarian", fill="black")
    canvas.itemconfig(word, text = new_card["Hungarian"], fill="black" )

    timer = window.after(3000, flip, new_card)

def flip(current_card):
    canvas.itemconfig(card, image = card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def known_word():
    global new_card
    data.remove(new_card)
    data_frame = pandas.DataFrame(data)
    data_frame.to_csv("./data/words_to_learn.csv", index=False)

    next_card()

#UI CONFIG

window = Tk()
window.title("Hungarian Flashcards")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card = canvas.create_image(400, 263, image=card_front_img)

title = canvas.create_text(400, 140, font=("Ariel", 40, "italic"))

word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

right_bt = Button(image=right_img, highlightthickness=0, command=known_word)
right_bt.grid(row=1, column=0)

wrong_bt = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_bt.grid(row=1, column=1)

timer = window.after(0, next_card)

window.mainloop()