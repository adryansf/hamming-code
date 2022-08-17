from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Notebook

# Components
from app.interface.components import Input
# App
from app.send import run as run_send
from app.utils.message import (incorrect_pos_message, send_message,
                               verify_message)
from app.verify import run as run_verify


class Interface:
    def __init__(self):
        window = Tk()
        window.geometry("600x230")
        window.resizable(False, False)
        window.title('CÓDIGO DE HAMMING')

        validation = window.register(self.keybind)

        # Gerar Abas
        tab_control = Notebook(window)

        tab_send = Frame(tab_control, pady=10, padx=10)
        tab_verify = Frame(tab_control, pady=10, padx=10)
        tab_credits = Frame(tab_control, pady=10, padx=10)
        tab_control.pack(expand=True, fill="both")

        tab_control.add(tab_send, text="Enviar um grupo de bits")
        tab_control.add(tab_verify, text="Verificar um grupo de bits recebido")
        tab_control.add(tab_credits, text="Créditos")

        # Aba Enviar
        self.input_send = Input.new(tab_send, "Bits")
        self.input_send["width"] = 400
        self.input_send["validate"] = "key"
        self.input_send["validatecommand"] = (validation, '%S')

        button_send = Button(tab_send, text="Enviar", width=20,
                             command=self.button_send_action, pady=5, border=2)

        self.text_send = Text(tab_send, bg="black", bd=1,
                              width=400, fg="white")
        self.text_send.configure(yscrollcommand=True)
        self.text_send.bind("<Key>", lambda e: 'break')

        # Render
        self.input_send.pack()
        button_send.pack(pady=10)
        self.text_send.pack()

        # Aba Verificar
        self.input_verify = Input.new(tab_verify, "Bits")
        self.input_verify["width"] = 400
        self.input_verify["validate"] = "key"
        self.input_verify["validatecommand"] = (validation, '%S')

        button_verify = Button(tab_verify, text="Verificar", width=20,
                               command=self.button_verify_action, pady=5, border=2)

        self.text_verify = Text(tab_verify, bg="black",
                                bd=1, width=400, fg="white")
        self.text_verify.configure(yscrollcommand=True)
        self.text_verify.bind("<Key>", lambda e: 'break')

        # Renderizar
        self.input_verify.pack()
        button_verify.pack(pady=10)
        self.text_verify.pack()

        # Aba Créditos
        text_credit = Label(tab_credits, width=400,
                            font=Font(size=12, weight="bold"))
        text_credit['text'] = "Trabalho desenvolvido por:\n\n Adryan Freitas\n\nKalebe Nascimento\n\nMaria Júlia Zabbal"
        text_credit.pack(pady=(15, 0))

        # Mantém a janela aberta
        window.mainloop()

    def button_send_action(self):
        data = self.input_send.get()
        result = run_send(data)
        self.text_send.delete('1.0', END)
        self.text_send.insert(INSERT, send_message(data, result))

    def button_verify_action(self):
        value = self.input_verify.get()
        result = run_verify(value)
        self.text_verify.delete('1.0', END)
        if (result["incorrect_pos"] != -1):
            self.text_verify.insert(
                INSERT, f'{incorrect_pos_message(result["incorrect_pos"], value)}\n')
        else:
            self.text_verify.insert(INSERT, "Não foi detectado erros!\n")
        self.text_verify.insert(
            INSERT, f'{verify_message(result["original_bits"])}\n')

    def keybind(self, e):
        return e == '1' or e == '0'
