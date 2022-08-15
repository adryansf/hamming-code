def run(value):
    bits = list(map(lambda v:  int(v), list(value)))
    qt_bits = len(bits)
    k = 1
    controlled_pos = list()
    value_parity = list()
    original_bits = list()
    parity_pos = list()
    incorrect_pos = -1

    while (qt_bits > pow(2, k) - 1):
        k += 1

    for i in range(k):
        jump = pow(2, i)
        initial_pos = jump - 1
        isFirst = 1
        qt_one = 0
        subPositions = list()
        # Percorre a lista de bits pulando de acordo com a paridade
        for j in range(initial_pos, qt_bits, jump * 2):
            # Varre os bits em sequência
            for l in range(j, j+jump):
                if (isFirst):
                    isFirst = 0
                    continue
                if (l > (qt_bits-1)):
                    break
                subPositions.append(l)
                if (bits[l] == 1):
                    qt_one += 1
        controlled_pos.append(subPositions)
        value_parity.append(0 if qt_one % 2 == 0 else 1)

    for index, p in enumerate(value_parity):
        if (p != bits[pow(2, index) - 1]):
            value_parity[index] = -1

    for index, p in enumerate(value_parity):
        if (p == -1):
            if (incorrect_pos == -1):
                incorrect_pos = 0
            incorrect_pos += pow(2, index)

    bits[incorrect_pos-1] = int(not bits[incorrect_pos-1])

    for i in range(k):
        parity_pos.append(pow(2, i) - 1)

    for index, bit in enumerate(bits):
        if index not in parity_pos:
            original_bits.append(bit)

    return {
        "incorrect_pos": incorrect_pos,
        "bits": bits,
        "original_bits": ''.join(str(b) for b in original_bits)
    }
