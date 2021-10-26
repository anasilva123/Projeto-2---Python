

# Questão 3
# Solicitar salario, perstaçao. Se prestação for maior que 20% do salario, imprimir : Empréstimo não pode ser concedido. Senão imprimir Empréstimo pode ser concedido.

salario = int(input(' Qual o valor do seu salário? '))
prestacao = int(input(' Qual o valor da prestação que você quer pagar? '))
if prestacao > salario * 0.20:
  print(' Infelizmente, você não pode realizar o empréstimo! ')
elif prestacao <= salario * 0.20:
  print(' Ótimo, seu empréstimo foi aprovado! ')


# Questão - 2
# Ler um ano de nascimento e ano atual. Imprimir a idade da pessoa. Se a idade for maior ou igual a 18 leia o nome da pessoa e imprima o nome digitado e uma mensagem informando que sua entrada é permitida. (Ex: Fulano, sua entrada foi permitida.)

nascimento = int(input(' Qual o ano do seu nascimento? '))
ano_atual = int(input(' Qual ano estamos? '))
idade = ano_atual - nascimento
print(idade)
if idade >= 18:
  print(' Sua entrada é permitida. ')
else:
  print(' Infelizmente você não pode entrar. ')


# Questão - 5
# Informar um número e imprimir se é par ou ímpar.

numero = float(input(' Digite um número: '))
resto = numero % 2
if resto == 0:
  print(' O número escolhido é par. ')
else:
  print(' O número escolhido é ímpar. ')


# Questão - 8
# Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

numero1 = int(input(' Escolha um número: '))
numero2 = int(input(' Escolha outro número: '))
numero3 = int(input(' Escolha mais um número: '))
maior = numero1
if numero2 > maior:
  maior = numero2
if numero3 > maior:
  maior = numero3
print(' O maior número escolhido foi: ',maior)


# Questão - 10
# Faça um algoritmo que leia dois números e indique se são iguais ou se são diferentes. Mostre o maior e o menor (nesta sequência).

numero1 = int(input(' Digite um número: '))
numero2 = int(input(' Digite outro número: '))
if numero1 == numero2:
  print(' Os números são iguais. ')
elif numero1 > numero2:
  print(' O primerio número é maior que o segundo número. ')
elif numero1 < numero2:
  print(' O segundo número é maior que o primeiro número. ')


# Questão - 9
# Faça um algoritmo que leia dois números nas variáveis NumA e NumB, nessa ordem, e imprima em ordem inversa, isto é, se os dados lidos forem NumA = 5 e NumB = 9, por exemplo, devem ser impressos na ordem NumA = 9 e NumB = 5.

numero_a = int(input(' Digite o número A: '))
numero_b = int(input(' Digite o número B: '))
print(' NumA = ', numero_b, ' e NumB = ',numero_a)


# Questão - 1
# Fazer um programa que imprima a média aritmética dos números8,9 e 7. A media dos números 4, 5 e 6. A soma das duas médias. A media das medias.

notas1 = int(8 + 9 + 7)
media1 = notas1 / 3
print(' A primeira média é:', media1)
notas2 = int(4 + 5 + 6)
media2 = notas2 / 3
print(' A segunda média é: ', media2)
mediana = media1 + media2
print(' A soma das duas médias é: ', mediana)
media_final = mediana / 2
print(' A média final é: ', media_final)


# Questão - 4
# Informar um saldo e imprimir o saldo com reajuste de 1%.

saldo = float(input(' Informe o valor do saldo atual: '))
print(' O saldo reajustado em 1% fica: ', saldo * (1 + 1/100))


# Questão - 6
# Ler 1 número. Se positivo, imprimir raiz quadrada senão o quadrado do número.

numero_z = int(input(' Digite um número aleatório: '))
if numero_z > 0:
 print(numero_z ** 0.5)
else:
  print(numero_z ** 2)

# Questão - 7
# Ler um número e imprimir igual a 20, menor que 20, maior que 20.

numero = int(input(' Digite um número: '))
if numero == 20:
  print(' Número igual a 20. ')
elif numero < 20: 
  print(' Número menor que 20. ')
elif numero > 20:
  print(' Número maior que 20. ')
