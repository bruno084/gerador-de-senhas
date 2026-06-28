import random
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numero = "0123456789"
todos_caracteres = letras + numero
quantidade_senhas = int(input("!! QUANTAS SENHAS VOCÊ QUER GERAR? !!"))
tamanho = int(input("!! QUANTOS CARACTERES CADA SENHA DEVE TER? !!"))
print("\n=== !! SUAS SENHAS GERADAS SÃO: !! ===")
for j in range(quantidade_senhas):
    senha = ""  
    for i in range(tamanho):
        senha += random.choice(todos_caracteres)

    print("Senha {}: {}".format(j + 1, senha))