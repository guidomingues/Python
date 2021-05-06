#5. Faça um programa que recebe um número inteiro e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.

n1=int(input('Entre com um número: '))
if n1 %10 ==0 or n1 %5 ==0 or n1 %2 ==0 :
    print('Número divisível por 10 e/ou por 5 e/ou por 2')
else:
    print('Não é divisível por nenhum destes')