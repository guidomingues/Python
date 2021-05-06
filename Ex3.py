#Faça um programa para ler um número e imprimir uma mensagem dizendo se o mesmo é par e positivo ao mesmo tempo.

n1=int(input('Entre com um número '))
if n1 % 2 ==0 and n1>0:
    print('O seu número é par e positivo')
else: 
    print('Seu número não é par ou não é positivo')