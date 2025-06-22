from itertools import product  # importa product pra gerar combinações
from time import time  # importa time pra contar o tempo
from sys import exit
user_senha = input('Digite sua senha: ')

if not user_senha:  # verifica se a senha não está vazia
    print("Senha não pode ser vazia.")
    exit()

# lista de caracteres para o brute force
caracteres = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?', '`', '~'
]

inicio = time()
tentativas = 0

# gera as combinações possíveis de caracteres com o tamanho da senha
for tentativa_tuple in product(caracteres, repeat=len(user_senha)):
    tent = ''.join(tentativa_tuple)  # converte a tupla para string
    tentativas += 1

    # verifica se a tentativa é igual à senha do usuário
    if tent == user_senha:
        fim = time()
        tempo_gasto = fim - inicio

        print(f'\nSenha encontrada: {tent}')
        print(f'Total de tentativas: {tentativas:,}'.replace(',', '.'))
        print(f'Tempo gasto: {tempo_gasto:.2f} segundos')
        break
