import itertools
import re

def calcula_digito(cpf):
    res = []
    for i, a in enumerate(cpf):
        b = len(cpf) + 1 - i
        res.append(b * a)

    res = sum(res) % 11

    if res > 1:
        return 11 - res
    else:
        return 0

def gera_cpfs_possiveis(digitos_meio):
    digitos_meio = [int(digito) for digito in digitos_meio]
    for inicio in itertools.product(range(10), repeat=3):
        for fim in itertools.product(range(10), repeat=2):
            cpf = list(inicio) + digitos_meio + list(fim)
            cpf_verificado = cpf[:9] + [calcula_digito(cpf[:9]), calcula_digito(cpf[:9] + [calcula_digito(cpf[:9])])]
            if cpf == cpf_verificado:
                yield ''.join(map(str, cpf))

digitos_meio = '334130'
for cpf in gera_cpfs_possiveis(digitos_meio):
    print(cpf)
    if cpf == '22433413010':
        print("=============================")
        print(cpf)
        print("=============================")

digitos_meio = '413470'
for cpf in gera_cpfs_possiveis(digitos_meio):
    print(cpf)
    if cpf == '28641347054':
        print("=============================")
        print(cpf)
        print("=============================")
