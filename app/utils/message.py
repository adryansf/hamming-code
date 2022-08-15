def send_message(data, result):
    return f'Dados Originais: {data}\nDados que serão enviados: {result}'


def verify_message(result):
    return f'Grupo de bits finais com o bit corrigido: {result}'


def incorrect_pos_message(pos, bits):
    return f'Foi detectado um erro no bit nº {pos} do grupo: {bits}'
