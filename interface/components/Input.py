from tkinter import Entry, Label
from tkinter.font import Font


def new(frame, label):
    font = Font(size=16)
    label = Label(frame, text=label, font=font).pack(pady=10)
    newInput = Entry(frame)
    return newInput
