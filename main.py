from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# --- PASSWORD GENERATOR --- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    random_letters = [choice(letters) for n in range(randint(8, 10))]
    random_numbers = [choice(numbers) for n in range(randint(2, 4))]
    random_symbols = [choice(symbols) for n in range(randint(2, 4))]

    random_password_list = random_letters + random_numbers + random_symbols
    shuffle(random_password_list)
    random_password = "".join(random_password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# --- SAVE PASSWORD --- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all the required fields.")

    else:
        save = messagebox.askokcancel(title=website, message=f"You entered...\n\nWebsite: {website}\n"
                                                             f"Username: {username}\nPassword: "
                                                             f"{password}\n\nDo you want to save?")
        if save:
            with open("data.txt", "a") as password_data:
                password_data.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


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
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Entries
password_entry = Entry(width=22, justify="center", fg="gray")
password_entry.grid(column=1, row=3)

username_entry = Entry(width=36, justify="center", fg="gray")
username_entry.grid(column=1, row=2, columnspan=2)

website_entry = Entry(width=36, justify="center", fg="gray")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Labels
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

username_label = Label(text="E-mail / Username:")
username_label.grid(column=0, row=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

canvas.mainloop()
