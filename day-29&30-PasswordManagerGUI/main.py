from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("Lucida Grande", 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if not website or not username or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it okay to save?")
        if is_ok:

            try:
                with open("data.json", "r") as data:
                    old_data = json.load(data)
                    old_data.update(new_data)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)

            else:
                with open("data.json", "w") as data:
                    json.dump(old_data, data, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCHING FOR PASSWORD ------------------------------- #
def find_passsword():
    website = website_entry.get()
    if website:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showwarning(title="Error", message="No data file found!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showwarning(title="Error", message=f"No details for the website exist!")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row = 1, column = 0)

name_label = Label(text="Email/Username:", font=FONT)
name_label.grid(row = 2, column = 0)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row = 3, column = 0)

website_entry = Entry()
website_entry.grid(row = 1, column = 1, sticky = EW)
website_entry.focus()

name_entry = Entry()
name_entry.grid(row = 2, column = 1, columnspan = 2, sticky = EW)
name_entry.insert(0, "vialligpd@gmail.com")

password_entry = Entry()
password_entry.grid(row = 3, column = 1, sticky = EW)

generate_bt = Button(text="Generate password", font=FONT, command=generate_password)
generate_bt.grid(row = 3, column = 2, sticky = EW)

add_bt = Button(text="Add", font=FONT, width = 36, command = save_password)
add_bt.grid(row = 4, column = 1, columnspan = 2, sticky = EW)

search_bt = Button(text="Search", font=FONT, command=find_passsword)
search_bt.grid(row = 1, column = 2, sticky = EW)

window.mainloop()