from tkinter import *

# --- PASSWORD GENERATOR --- #

# --- SAVE PASSWORD --- #

# --- UI SETUP --- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Buttons
add_button = Button(text="Add", width=37)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

# Entries
password_entry = Entry(width=22, justify="center", fg="gray")
password_entry.insert(END, "* Required")
password_entry.grid(column=1, row=3)

username_entry = Entry(width=36, justify="center", fg="gray")
username_entry.insert(END, "* Required")
username_entry.grid(column=1, row=2, columnspan=2)

website_entry = Entry(width=36, justify="center", fg="gray")
website_entry.insert(END, "* Required")
website_entry.grid(column=1, row=1, columnspan=2)

# Labels
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

username_label = Label(text="E-mail / Username:")
username_label.grid(column=0, row=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

canvas.mainloop()
