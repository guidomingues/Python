#9. Criar uma função que recebe o peso e a altura e retorna o valor do seu IMC. onde IMC=peso/altura²

def imc(peso,altura): 
    imc=peso/altura**2
    print('Seu IMC é: ',imc)
imc(80,1.80)