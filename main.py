from tkinter import *
from tkinter import messagebox
from tkinter.tix import _dummyComboBox, ComboBox
from tkinter.ttk import Combobox

import requests


# converter start
converter = Tk()
converter.geometry("900x400")
converter.title("Currency Converter")
converter["bg"] = "blue"
currencies = []
prices = []
# Functions start


def usd_activation():
    en_Other["state"] = "normal"
    en_Other.delete(0, END)
    en_Other["state"] = "readonly"

    btn_C_Other["state"] = "disable"

    out_Other["state"] = "normal"
    out_Other.delete(0, END)
    out_Other["state"] = "readonly"

    en_USD["state"] = "normal"
    en_USD.delete(0, END)

    btn_C_USD["state"] = "normal"

    out_USD["state"] = "normal"
    out_USD.delete(0, END)
    out_USD["state"] = "readonly"


def other_activation():
    en_USD["state"] = "normal"
    en_USD.delete(0, END)
    en_USD["state"] = "readonly"

    btn_C_USD["state"] = "disable"

    out_USD["state"] = "normal"
    out_USD.delete(0, END)
    out_USD["state"] = "readonly"

    en_Other["state"] = "normal"
    en_Other.delete(0, END)

    btn_C_Other["state"] = "normal"

    out_Other["state"] = "normal"
    out_Other.delete(0, END)
    out_Other["state"] = "readonly"


def usd_cal():
    out_USD["state"] = "normal"
    out_USD.delete(0, END)
    out_USD["state"] = "readonly"
    INDEX = -1
    try:
        for k in range(len(currencies)):
            if currencies[k] == cmb_currencies.get():
                INDEX = k
        if INDEX != -1:
            if en_USD.get() != "":
                cost = str(int(float(en_USD.get()) * float(prices[INDEX])))
                cost = cost + " " + currencies[INDEX]
                out_USD["state"] = "normal"
                out_USD.insert(0, cost)
                out_USD["state"] = "readonly"
            else:
                messagebox.showerror("Error", "Enter the Amount")
        else:
            messagebox.showerror("Error", "Please choose a valid Currency")
    except ValueError as ve:
        messagebox.showerror("Error", ve)

def other_cal():
    out_Other["state"] = "normal"
    out_Other.delete(0, END)
    out_Other["state"] = "readonly"
    INDEX = -1
    try:
        for k in range(len(currencies)):
            if currencies[k] == cmb_currencies.get():
                INDEX = k
        if INDEX != -1:
            if en_Other.get() != "":
                cost = str(int(float(en_Other.get()) / float(prices[INDEX])))
                cost = cost + " USD"
                out_Other["state"] = "normal"
                out_Other.insert(0, cost)
                out_Other["state"] = "readonly"
            else:
                messagebox.showerror("Error", "Enter the Amount")
        else:
            messagebox.showerror("Error", "Please choose a valid Currency")
    except ValueError as ve:
        messagebox.showerror("Error", ve)


def clear():
    en_USD["state"] = "normal"
    en_USD.delete(0, END)
    en_USD["state"] = "readonly"

    btn_C_USD["state"] = "disable"

    out_USD["state"] = "normal"
    out_USD.delete(0, END)
    out_USD["state"] = "readonly"

    en_Other["state"] = "normal"
    en_Other.delete(0, END)
    en_Other["state"] = "readonly"

    btn_C_Other["state"] = "disable"

    out_Other["state"] = "normal"
    out_Other.delete(0, END)
    out_Other["state"] = "readonly"


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        converter.destroy()


# Functions end
try:
    r = requests.get("https://v6.exchangerate-api.com/v6/87b4ad8e09c6667f61028d33/latest/USD")
    data = r.json()
    for key in data["conversion_rates"].keys():
        currencies.append(key)
    for value in data["conversion_rates"].values():
        prices.append(value)
except requests.exceptions.ConnectionError:
    messagebox.showerror("Network Error", "You have no internet connection")
    exit()


lbl_Head = Label(converter, text="Currency Converter", bg="blue")
lbl_Head["font"] = "Times", 20
lbl_Head.place(x=350, y=10)

# Label Frames start
lf_USD = LabelFrame(converter, text="United States Dollar", borderwidth=10, font=("Times", 10))
lf_USD["bg"] = "white"
lf_USD.place(x=100, y=100, height=100, width=300)

lf_Other = LabelFrame(converter, text="Other", borderwidth=10, font=("Times", 10))
lf_Other["bg"] = "White"
lf_Other.place(x=500, y=100, height=100, width=300)
# Label Frames end

# Inputs start
en_USD = Entry(lf_USD)
en_USD["font"] = "Times", 10
en_USD.place(x=10, y=10, width=200)

en_Other = Entry(lf_Other)
en_Other["font"] = "Times", 10
en_Other.place(x=10, y=10, width=200)
# Inputs end

# Activate Buttons start
btn_A_USD = Button(lf_USD, text="Activate", bg="blue")
btn_A_USD["command"] = usd_activation
btn_A_USD["font"] = "Times", 10
btn_A_USD.place(x=10, y=35, width=100)

btn_A_Other = Button(lf_Other, text="Activate", bg="blue")
btn_A_Other["command"] = other_activation
btn_A_Other["font"] = "Times", 10
btn_A_Other.place(x=10, y=35, width=100)
# Activate Buttons end

# Combobox start
cmb_currencies = Combobox(lf_Other)
cmb_currencies["values"] = currencies
cmb_currencies.place(x=220, y=10, width=50)
cmb_currencies["state"] = "readonly"
# Combobox end

# Calculate Buttons start
btn_C_USD = Button(lf_USD, text="Calculate", bg="blue")
btn_C_USD["command"] = usd_cal
btn_C_USD["font"] = "Times", 10
btn_C_USD.place(x=170, y=35, width=100)

btn_C_Other = Button(lf_Other, text="Calculate", bg="blue")
btn_C_Other["command"] = other_cal
btn_C_Other["font"] = "Times", 10
btn_C_Other.place(x=170, y=35, width=100)
# Calculate Buttons end

# Outputs start
out_Other = Entry(converter)
out_Other["font"] = "Times", 20
out_Other.place(x=550, y=210, width=200, height=50)

out_USD = Entry(converter)
out_USD["font"] = "Times", 20
out_USD.place(x=150, y=210, width=200, height=50)
# Outputs end

# Default state start
en_Other["state"] = "readonly"
en_USD["state"] = "readonly"
btn_C_USD["state"] = "disable"
btn_C_Other["state"] = "disable"
out_USD["state"] = "readonly"
out_Other["state"] = "readonly"
# Default state end

# command Buttons start
btn_Clear = Button(converter, text="Clear", borderwidth=5, font=("Times", 10))
btn_Clear["bg"] = "White"
btn_Clear["command"] = clear
btn_Clear.place(x=100, y=300, width=300)

btn_Exit = Button(converter, text="Exit Program", borderwidth=5, font=("Times", 10))
btn_Exit["bg"] = "White"
btn_Exit["command"] = ex
btn_Exit.place(x=500, y=300, width=300)
# command Buttons end

converter.mainloop()
# Converter End
