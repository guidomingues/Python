#7. Faça uma função que receba o salário de um funcionário. Sabendo que o salário do funcionário teve um aumento de 25%, calcular e retornar o novo salário.

def novoSal(sal):
    novoSal=sal*0.25+sal
    print('Seu novo salário é: ',novoSal)
novoSal(1000)