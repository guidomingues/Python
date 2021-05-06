#7. Fazer um programa que leia um valor de DDI e informe o nome do país
# Correspondente ao DDI. Por exemplo: Se ler 1 imprime "Estados Unidos", 49 "Alemanha", 54 "Argentina", 55 "Brasil", 35 "Portugal". Deve também imprimir uma mensagem caso o DDI não esteja cadastrado.

ddi=int(input('Informe seu DDI: '))
if ddi==1:
    print('Estados Unidos')
elif ddi==49:
    print('Alemanha')
elif ddi==54:
    print('Argentina')
elif ddi==55:
    print('Brasil')
elif ddi==35:
    print('Portugal')
else: 
    print('DDI não cadastrado')