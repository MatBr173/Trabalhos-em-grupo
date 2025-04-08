import random

nove_digito = ''
for i in range(9):
    nove_digito += str(random.randint(0, 9))        

contagem_regressiva_1 = 10
soma_1 = 0

for digito_1 in nove_digito:
    soma_1 = (int(digito_1) * contagem_regressiva_1) + soma_1
    contagem_regressiva_1 -= 1
digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

str(digito_1)
dez_digitos = nove_digito, digito_1
contagem_regressiva_2 = 11
soma_2 = 0
res = ''.join(map(str, dez_digitos))

for digito_2 in res:
    soma_2 = (int(digito_2) * contagem_regressiva_2) + soma_2
    contagem_regressiva_2 -= 1
digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
str(digito_2)
print(res, digito_2, sep='')