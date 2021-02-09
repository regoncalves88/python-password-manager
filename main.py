from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

    new_data = {
        website: {
            "username": username,
            "password": password,
        },
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all the required fields.")
    else:
        save = messagebox.askokcancel(title=website, message=f"You entered...\n\nWebsite: {website}\n"
                                                             f"Username: {username}\nPassword: "
                                                             f"{password}\n\nDo you want to save?")

        if save:
            try:
                with open("data.json", "r") as password_data:
                    data = json.load(password_data)
            except FileNotFoundError:
                with open("data.json", "w") as password_data:
                    json.dump(new_data, password_data, indent=4)
            else:
                with open("data.json", "w") as password_data:
                    data.update(new_data)
                    json.dump(data, password_data, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# --- SAVE PASSWORD --- #
def search_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please fill in the Website field.")
    else:
        try:
            with open("data.json", "r") as password_data:
                data = json.load(password_data)

                if website in data.keys():
                    username = data[website]["username"]
                    password = data[website]["password"]
                    messagebox.showinfo(title=website, message=f"Website: {website}\nUsername: {username}\n"
                                                               f"Password: {password}")
                    pyperclip.copy(password)
                else:
                    messagebox.showerror(title="Error", message=f'The website "{website}" is not yet registered.')
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No websites yet registered.")


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

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)

# Entries
password_entry = Entry(width=22, justify="center", fg="gray")
password_entry.grid(column=1, row=3)

username_entry = Entry(width=36, justify="center", fg="gray")
username_entry.grid(column=1, row=2, columnspan=2)

website_entry = Entry(width=22, justify="center", fg="gray")
website_entry.focus()
website_entry.grid(column=1, row=1)

# Labels
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

username_label = Label(text="E-mail / Username:")
username_label.grid(column=0, row=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

canvas.mainloop()
