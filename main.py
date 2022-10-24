from tkinter import *
import random
from tkinter import messagebox

# from ctypes import windll

# import pandas

# windll.shcore.SetProcessDpiAwareness(1)

CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
              '%', '&', '(', ')', '*', '+']

BACKGROUND_COLORS = ['#1eb7ed', '#1ca2eb', '#b3d4fc', '#2581fe', '#ff0853', '#01147b', '#81d135', '#25d366']
BACKGROUND_COLOR = random.choice(BACKGROUND_COLORS)
FONT = ("Segoe UI", 10)


# password_dictionary = {
#     "website": [],
#     "username": [],
#     "password": [],
# }


def add_password():
    # global password_dictionary
    # password_dictionary["website"].append(website_text.get())
    # password_dictionary["username"].append(username_text.get())
    # password_dictionary["password"].append(password_text.get())
    # password_data = pandas.DataFrame(password_dictionary)
    # password_data.to_csv("passwords.csv", mode="a")
    # print(password_data)

    if website_text.get() == "" or username_text.get() == "" or password_text.get() == "":
        messagebox.showinfo(title="Bad user!", message="Don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=f"{website_text.get()}", message=f"Email/Username: {username_text.get()}\n"
                                                                              f" Password: {password_text.get()}\nDo "
                                                                              f"you want to save?")
        if is_ok:
            passwords = f"{website_text.get()}  |  {username_text.get()}  |  {password_text.get()}"
            with open("passwords.txt", "a") as file:
                file.write(f"{passwords}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    password = ""
    for i in range(16):
        password += random.choice(CHARACTERS)
    password_text.set(password)
    window.clipboard_clear()
    window.clipboard_append(password_text.get())
    window.update()


window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, background=BACKGROUND_COLOR)

website_label = Label(text="Website:", font=FONT, width=15, relief="solid", bg="#FFFFFF")
website_label.grid(column=0, row=0, padx=10, pady=10)
username_label = Label(text="Username/Email:", font=FONT, width=15, relief="solid", bg="#FFFFFF")
username_label.grid(column=0, row=1, pady=10, padx=10)
password_label = Label(text="Password:", font=FONT, width=15, relief="solid", bg="#FFFFFF")
password_label.grid(column=0, row=2, padx=10, pady=10)

website_text = StringVar()
website_entry = Entry(textvariable=website_text, relief="solid", bg="#FFFFFF", highlightthickness=1,
                      highlightbackground="black")
website_entry.grid(column=1, row=0, pady=10, padx=10)
website_entry.focus()

username_text = StringVar()
username_entry = Entry(textvariable=username_text, relief="solid", bg="#FFFFFF", highlightthickness=1,
                       highlightbackground="black")
username_entry.grid(column=1, row=1, pady=10, padx=10)

password_text = StringVar()
password_entry = Entry(textvariable=password_text, relief="solid", bg="#FFFFFF", highlightthickness=1,
                       highlightbackground="black")
password_entry.grid(column=1, row=2, pady=10, padx=10)

add_button = Button(text="Add password", font=FONT, width=15, height=1, relief="solid", bg="#FFFFFF",
                    command=add_password)
add_button.grid(column=0, row=3, pady=10, padx=10)
generate_button = Button(text="Generate password", font=FONT, width=18, height=1, relief="solid", bg="#FFFFFF",
                         command=generate_password)
generate_button.grid(column=1, row=3, pady=10, padx=10)

window.mainloop()
