from tkinter import *
import pandas
import random
import atexit


BACKGROUND_COLOR = "#B1DDC6"
def save_words_to_learn():
    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)

atexit.register(save_words_to_learn)

def import_data():
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
        if data.empty:
            raise pandas.errors.EmptyDataError
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        data = pandas.read_csv("data/french_words.csv")
    return data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def known_word():
    data_dict.remove(current_card)
    next_card()


data_dict = import_data()
current_card = {}

window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button images
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, relief="flat", bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, relief="flat", bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=known_word)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()

