valores = []
maior = []
menor = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um numero na posicao {cont}: ')))

print('=-' * 30)
print(f'Você digitou os valores {valores} ')

for pos, v in enumerate(valores):
    if v == max(valores):
        maior.append(pos)
    if v == min(valores):
        menor.append(pos)

print(f'o maior valor foi {max(valores)}, na posição {maior}')
print(f'o menor numero foi {min(valores)}, na posição {menor}')