from tkinter import *
import random
import pandas



BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
WORD_SIZE = 60
WORD_THICKNESS = "bold"
TITLE_SIZE = 40
TITLE_THICKNESS = "italic"

current_card = {}
known_words = {}


try:

    to_learn = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    all_french_words = pandas.read_csv('data/french_words.csv')
    known_words = all_french_words.to_dict(orient="records")
else:
    known_words = to_learn.to_dict(orient='records')





def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(known_words)
    fr_word = current_card['French']
    canvas.itemconfig(card_front, image=card_front_image)
    canvas.itemconfig(title_image, text='French', fill='black')
    canvas.itemconfig(word_image, text=fr_word, fill='black')
    flip_timer = window.after(3000, flip_card)

def is_known():
    known_words.remove(current_card)
    next_card()
    data = pandas.DataFrame(known_words)
    data.to_csv("data/words_to_learn", index=False)


def flip_card():
    canvas.itemconfig(title_image, text='English', fill='white')
    canvas.itemconfig(word_image, text=current_card['English'], fill='white')
    canvas.itemconfig(card_front, image=card_back_image)










window = Tk()
window.title("Test")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)




card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

# Card front
card_front = canvas.create_image(400, 263, image=card_front_image)
title_image = canvas.create_text(400, 150, text="", font=(FONT, TITLE_SIZE, TITLE_THICKNESS))
word_image = canvas.create_text(400, 263, text="", font=(FONT, WORD_SIZE, WORD_THICKNESS))
canvas.grid(column=1, row=1, columnspan=2)

# Card back






# right
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=2)




# Wrong
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=2, row=2)


next_card()

window.mainloop()