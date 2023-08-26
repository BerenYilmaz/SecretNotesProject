from tkinter import *
import pybase64
from tkinter import messagebox


window = Tk()
window.title("Crypted")
window.minsize(width=400, height=700)

#Image
img = PhotoImage(file='download2.png',width=100,height=100)
Label(window,image=img).pack()

title_label = Label(text="Enter Your Title")
title_label.config(font=('Arial', 20))
title_label.pack()

title_entry = Entry()
title_entry.config()
title_entry.pack()

title_label_2 = Label(text="Tell Me You Can Trust Me")
title_label_2.config(font=('Arial', 13))
title_label_2.pack()

secret_text = Text(width=30,height=20)
secret_text.pack()

enter_master_key = Label(text="Enter Master Key", font=('Arial', 12))
enter_master_key.pack()

master_key_entry = Entry()
master_key_entry.pack()

def encrypt():
    secret = secret_text.get(1.0,END)

    secret_text.delete(1.0, END)
    if master_key_entry.get() == "beren":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        secret_text.insert(END, secret)
    else:
        messagebox.showwarning("Incorrect!", "Incorrect password who are you!!")
def decrypt():
    secret = secret_text.get(1.0, END)
    secret_text.delete(1.0, END)

    if master_key_entry.get() == "beren":
        secret = secret.encode("ascii")
        secret = pybase64.b64decode(secret)
        secret = secret.decode("ascii")
        secret_text.insert(END, secret)

    else:
        messagebox.showwarning("Incorrect!", "Incorrect password who are you!!")


encrypt_button = Button(text="Save & Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt)
decrypt_button.pack()



window.mainloop()