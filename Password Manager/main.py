from tkinter import *
import random
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    new_password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, new_password)
    password_input.clipboard_clear()
    password_input.clipboard_append(string=new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    n_website = website_input.get()
    n_email = email_input.get()
    n_password = password_input.get()
    new_data = {
        n_website: {
            "email": n_email,
            "password": n_password,
        }
    }
    if len(n_website) == 0 or len(n_password) == 0:
        messagebox.showinfo(title="Warning", message="Fields cannot be left blank, please enter info into each field.")
    else:
        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def search():
    website = website_input.get()
    try:
        with open("./data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Uh oh!", message=f"There is no data file yet.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Uh oh!", message=f"There is no Website: {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# ------CREATE LOGO IMAGE ON SCREEN-------
canvas = Canvas(height=200, width=200)
canvas.config()
logo_img = PhotoImage(file="logo.png")
canvas.create_image(50, 100, image=logo_img)
canvas.grid(column=1, row=0)
# ----------------------------------------

# ------CREATE LABELS ON SCREEN-----------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=E)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)
#-----------------------------------------

# ------CREATE INPUTS ON SCREEN-----------
website_input = Entry(width=32)
website_input.grid(column=1, row=1, columnspan=2, sticky=W)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2, sticky=W)
email_input.insert(0, STATIC_EMAIL)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2, sticky=W)
#-----------------------------------------

# ------CREATE BUTTONS ON SCREEN----------
search_button = Button(text="Search", command=search)
search_button.grid(column=1, row=1, columnspan=2, sticky=E)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=3, columnspan=2, sticky=E)
add_button = Button(text="Add", command=save_password, width=48)
add_button.grid(column=0, row=4, columnspan=2, sticky=W)
#-----------------------------------------

window.mainloop()
