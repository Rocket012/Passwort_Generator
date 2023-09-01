#make a password generator with tkinter in python

import tkinter as tk
import random
import string

#window
window: tk.Tk = tk.Tk()
window.geometry("400x400")
window.title("Password Generator")

#heading
heading: tk.Label = tk.Label(
    window, text="Password Generator", font=('arial 15 bold'), fg="green"
).pack()

#label
label1: tk.Label = tk.Label(
    window, text="Password Length", font=('arial 10 bold')
).pack()
label2: tk.Label = tk.Label(
    window, text="Password Strength", font=('arial 10 bold')
).pack()

#password length
pass_len: tk.IntVar = tk.IntVar()
length: tk.Scale = tk.Scale(
    window, from_=0, to=100, variable=pass_len, orient=tk.HORIZONTAL
).pack()

#password strength
pass_str: tk.StringVar = tk.StringVar()
radio_button1: tk.Radiobutton = tk.Radiobutton(
    window, text="Weak", variable=pass_str, value="weak", font=('arial 10 bold')
).pack()
radio_button2: tk.Radiobutton = tk.Radiobutton(
    window, text="Medium", variable=pass_str, value="medium", font=('arial 10 bold')
).pack()
radio_button3: tk.Radiobutton = tk.Radiobutton(
    window, text="Strong", variable=pass_str, value="strong", font=('arial 10 bold')
).pack()

#function
password: str = ""
def generate_password():
    global password
    password = ""
    if pass_len.get() <= 0:
        password = "Password length cannot be zero"
    else:
        for x in range(0, pass_len.get()):
            password = password + random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
    label3: tk.Label = tk.Label(window, text=password, font=('arial 10 bold')).pack()

#button
button1: tk.Button = tk.Button(
    window, text="Generate Password", command=generate_password
).pack()

#loop
window.mainloop()

#end of code