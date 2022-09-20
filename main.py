from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- EXTRACT WORDS FROM CSV ----------------------- #
french_words = pd.read_csv("data/french_words.csv")
selected_word = french_words.sample()
selected_word_french = selected_word.French.item()
selected_word_english = selected_word.English.item()


# ----------------------- NEXT WORD LOGIC ----------------------- #
def next_word():
    selected_new_word = french_words.sample()
    new_word_french = selected_new_word.French.item()
    global selected_word_french
    selected_word_french = new_word_french
    new_word_english = selected_new_word.English.item()
    global selected_word_english
    selected_word_english = new_word_english

    canvas_front.create_image(400, 263, image=card_photo_front)
    canvas_front.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    canvas_front.create_text(400, 263, text=selected_word_french, font=("Ariel", 60, "bold"))

    window.after(3000, switch_sides)


# ----------------------- FLASH CARDS LOGIC ----------------------- #
def switch_sides():
    canvas_front.create_image(400, 263, image=card_photo_back)
    canvas_front.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
    canvas_front.create_text(400, 263, text=selected_word_english, font=("Ariel", 60, "bold"))


# ----------------------- SETUP UI ----------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

card_photo_front = PhotoImage(file="images/card_front.png")
card_photo_back = PhotoImage(file="images/card_back.png")

canvas_front = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

canvas_front.create_image(400, 263, image=card_photo_front)
canvas_front.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_front.create_text(400, 263, text=selected_word_french, font=("Ariel", 60, "bold"))

canvas_front.grid(column=0, row=0, columnspan=2)

window.after(3000, switch_sides)

button_no_image = PhotoImage(file="images/wrong.png")
button_no = Button(image=button_no_image, highlightthickness=0, command=next_word)
button_no.grid(column=0, row=1)

button_yes_image = PhotoImage(file="images/right.png")
button_yes = Button(image=button_yes_image, highlightthickness=0, command=next_word)
button_yes.grid(column=1, row=1)

window.mainloop()
