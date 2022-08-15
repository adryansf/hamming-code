def run(value):
    qt_data = len(value)
    n = 0
    k = 1

    while (n < qt_data):
        k = k + 1
        n = pow(2, k) - k - 1

    total_bits = qt_data+k
    bits = list(map(lambda v:  int(v), list(value)))
    for i in range(0, k):
        bits.insert(pow(2, i)-1, 'p')

    # Um for para cada bit de paridade
    for i in range(0, k):
        jump = pow(2, i)
        initial_pos = jump - 1
        qt_one = 0
        # Percorre a lista de bits pulando de acordo com a paridade
        for j in range(initial_pos, total_bits, jump * 2):
            # Varre os bits em sequência
            for l in range(j, j+jump):
                if (l > (total_bits-1)):
                    break
                if (bits[l] == 1):
                    qt_one += 1
        bits[initial_pos] = 0 if qt_one % 2 == 0 else 1
    return ''.join(str(b) for b in bits)
