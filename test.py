value = '00010011011'


def verify(value):
    r = len(value)
    kList = []

    for i in range(r):
        kList.append(pow(2, i))
        if (pow(2, i) - i - 1) >= r:
            k = i

    res = []

    for i in range(k):
        aux = 0
        for j in range(1, r + 1, kList[i]):
            if j not in kList and j != kList[i]:
                aux = aux ^ int(value[j - 1])
        if aux != value[i - 1]:
            res.append(aux)

    return res


print(verify(value))
