from app.send import run as send_run
from app.utils.message import (incorrect_pos_message, send_message,
                               verify_message)
from app.verify import run as verify_run


def run():
    option = 0
    while (option != '3'):
        print('..:: GERADOR E VERIFICADOR DE CODIGO DE HAMMING ::..')
        print('Digite o que voce deseja fazer:')
        print("1) Enviar um grupo de bits")
        print('2) Verificar um grupo de bits recebido')
        print('3) Sair')
        option = input('Opçao: ')
        if (option != '3' and option != '1' and option != '2'):
            print('Opção inválida!')
        if (option == '1'):
            send_option()
        elif (option == '2'):
            verify_option()
        elif (option == '3'):
            print('FIM!')


def send_option():
    repeat = 1
    while (repeat):
        repeat = 0
        bits = input('Digite a quantidade de bits do grupo original: ')
        for b in list(bits.strip(" ")):
            if (b != '1' and b != '0'):
                repeat = 1
                break

        if (not repeat):
            result = send_run(bits)
            print(send_message(bits, result))
        else:
            print('Bits invalidos! Tente novamente!')


def verify_option():
    repeat = 1
    while (repeat):
        repeat = 0
        bits = input('Digite a quantidade de bits que foram recebidos: ')
        for b in list(bits.strip(" ")):
            if (b != '1' and b != '0'):
                repeat = 1
                break

        if (not repeat):
            result = verify_run(bits)
            if (result["incorrect_pos"] != -1):
                print(incorrect_pos_message(result["incorrect_pos"], bits))
            else:
                print("Nao foi detectado erros!")
            print(verify_message(result["original_bits"]))
        else:
            print('Bits invalidos! Tente novamente!')
    pass
