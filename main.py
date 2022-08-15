from app.interface.draw import Interface
from app.terminal.main import run as run_terminal

answer = False
while (answer != 'S' and answer != 'N'):
    answer = input('Deseja utilizar uma interface ? (S/N) ').upper()
    if (answer == 'S'):
        Interface()
    elif (answer == 'N'):
        run_terminal()
    else:
        print('Não foi possível compreender!')
