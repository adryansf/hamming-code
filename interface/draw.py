from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Notebook

# App
from app.send import calc

# Components
from interface.components import Input


# Actions
def buttonSendAction():
    result = calc(inputSend.get())
    textSend.delete('1.0', END)
    textSend.insert(INSERT, result)


def buttonVerifyAction():
    result = calc(inputVerify.get())
    textVerify.delete('1.0', END)
    textVerify.insert(INSERT, result)


def keybind(e):
    return e == '1' or e == '0'


# Inicia uma nova janela
window = Tk()
window.geometry("500x200")
window.resizable(False, False)
window.title('CÓDIGO DE HAMMING')

validation = window.register(keybind)

# Gerar Abas
tabControl = Notebook(window)

tabSend = Frame(tabControl, pady=10, padx=10)
tabVerify = Frame(tabControl, pady=10, padx=10)
tabCredits = Frame(tabControl, pady=10, padx=10)
tabControl.pack(expand=True, fill="both")

tabControl.add(tabSend, text="Enviar um grupo de bits")
tabControl.add(tabVerify, text="Verificar um grupo de bits recebido")
tabControl.add(tabCredits, text="Créditos")

# TabSend
inputSend = Input.new(tabSend, "Bits")
inputSend["width"] = 400
inputSend["validate"] = "key"
inputSend["validatecommand"] = (validation, '%S')

buttonSend = Button(tabSend, text="Enviar", width=20,
                    command=buttonSendAction, pady=5, border=2)

textSend = Text(tabSend, bg="black", bd=1, width=400, fg="white")
textSend.configure(yscrollcommand=True)
textSend.bind("<Key>", lambda e: 'break')

# Render
inputSend.pack()
buttonSend.pack(pady=10)
textSend.pack()


# TabVerify
inputVerify = Input.new(tabVerify, "Bits")
inputVerify["width"] = 400
inputVerify["validate"] = "key"
inputVerify["validatecommand"] = (validation, '%S')

buttonVerify = Button(tabVerify, text="Verificar", width=20,
                      command=buttonVerifyAction, pady=5, border=2)

textVerify = Text(tabVerify, bg="black", bd=1, width=400, fg="white")
textVerify.configure(yscrollcommand=True)
textVerify.bind("<Key>", lambda e: 'break')

# Render
inputVerify.pack()
buttonVerify.pack(pady=10)
textVerify.pack()

# Tab Credits
textCredit = Label(tabCredits, width=400, font=Font(size=12, weight="bold"))
textCredit['text'] = "Trabalho desenvolvido por:\n\n Adryan Freitas\n\nKalebe Nascimento\n\nMaria Júlia Zabbal"
textCredit.pack(pady=(15, 0))


# Mantém a janela aberta
window.mainloop()
