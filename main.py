BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

def next_card():
    pass

window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button images
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, relief="flat", bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, relief="flat", bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
right_button.grid(row=1, column=1)

window.mainloop()

