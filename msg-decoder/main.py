from tkinter import *
from tkinter import messagebox
import base64
import os

# function to encrypt message
def encrypt_msg():
    # get password
    password = code.get()
    if password == "1234":
        # secondary screen for encryption
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#186049")
        message = text1.get(1.0, END)
        # encode the message
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_msg = base64_bytes.decode("ascii")
        # label for encryption screen
        Label(screen1, text="Encrypted Message", font="arial", fg="white", bg="#186049").place(x=10, y=0)
        # output as read only textbox
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt_msg)
    # if empty password field
    elif password == "":
        messagebox.showerror("Encryption", "Please enter password")
    # if password not matching
    elif password != "1234":
        messagebox.showerror("Encryption", "Enter valid password")

# function to decrypt message
def decrypt_msg():
    password = code.get()
    if password == "1234":
        # secondary screen for decryption
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#0F42C0")
        message = text1.get(1.0, END)
        # decode the message
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_msg = base64_bytes.decode("ascii")
        # label for decryption screen
        Label(screen2, text="Decrypted Message", font="arial", fg="white", bg="#0F42C0").place(x=10, y=0)
        # output as read only textbox
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt_msg)
    # error conditions
    elif password == "":
        messagebox.showerror("Encryption", "Please enter password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Enter valid password")

def home_screen():
    global screen
    global code
    global text1
    # initialize home screen
    screen = Tk()
    screen.geometry("375x400")
    screen.title("Message Decoding App")
    # function to clear input field
    def clear_all():
        code.set("")
        text1.delete(1.0, END)
    # text input area
    Label(text="Enter text for encryption / decryption", fg="black", font=("arial", 12)).place(x=10, y=10)
    # multi line input area
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Label(text="Enter secret encryption key", fg="black", font=("arial, 12")).place(x=10, y=170)
    # password 
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 20), show="*").place(x=10, y=200, width=355)
    # buttons for encrypt, decrypt and clear with their function trigger
    Button(text="ENCRYPT", height="2", width=23, bg="#186049", fg="white", bd=0, command=encrypt_msg).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#0F42C0", fg="white", bd=0, command=decrypt_msg).place(x=200, y=250)
    Button(text="CLEAR", height="2", width=50, bg="#E00000", fg="white", bd=0, command=clear_all).place(x=10, y=300)

    screen.mainloop()

home_screen()