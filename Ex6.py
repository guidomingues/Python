#6. Um comerciante comprou um produto e quer vendê‐lo com lucro de 45% se o valor da compra for menor que 20,00; caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.

n1=int(input('Qual o valor do produto pago: '))
lucro1 = n1*0.45+n1
lucro2 = n1*0.30+n1
if n1<21:
    print('O valor para venda é de: ',lucro1)
else:
    print('O valor para venda é de: ',lucro2)
