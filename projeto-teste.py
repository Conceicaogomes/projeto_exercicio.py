# Crie um programa que solicite ao usuário informações como nome, idade e altura, 
# e utilize essas variáveis para exibir uma mensagem personalizada.

idade = int(input('Digite sua idade '))

if idade >= 18:
    nome = (input('Digite seu nome '))
    altura = float (input('Digite sua altura '))
    print('Cadastro concluido')

else:
 print("Você precisa ter 18 anos para se cadastrar! ")