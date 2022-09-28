'''
# 1) exiba uma string  
    print("ola mundo!")

# 2)  exiba o numero
    Numero = input("Favor digite um numero de 1 ate 10:  ")
    print(Numero)

# 3) soma de notas 
    numero01 = int (input("digite o primeiro numero: "))
    numero02 = int (input("digite o segundo numero: "))
    soma = numero01+numero02
    print(soma)

# 4) Media de notas  
    Nota1 = int (input("Digite a primeira nota: "))
    Nota2 = int (input("Digite a segunda nota: "))
    Nota3 = int (input("Digite a terceira nota: "))
    Nota4 = int (input("Digite a quarta nota: "))

media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
print(media)

# 5) metro para centimetro 
    mt = float(input("Digite a metragem desejada:  "))
    cm = (mt * 100)
    print("Valor convertido para centimetro:  ",cm,"cm")

# 6) area de um circulo
    diametro = float(input("Qual é o diametro do circulo?  "))
    raio = diametro / 2
    area = (raio * raio) * 3.14
    print(area)

# 7) area de um quadrado
lado = float(input("digite o lado do quadrado:  "))
area = lado * lado
print(area)

# 8) Calculo de salário
v_hora = float(input("Digite o valor da hora trabalhada:  "))
t_hora = float(input("Digite sua carga horaria mensal:  "))
v_salario = v_hora * t_hora
print(v_salario)

# 9) temperatura fahrenheit = celsius
fa = float(input("Digite a temperatura em F°:  "))
ce = 5* ((fa-32)/9)
print(ce,"C°")

# 10) temperatura celsius = fahrenheit
ce = float(input("Digite a temperatura em C°:  "))
fa = ((ce * 9)/5) + 32
print(fa, "F°")

# 11) Operações numeros inteiros e reais
ni1 = int(input("Digite um valor inteiro: "))
ni2 = int(input("Digite o segundo valor inteiro: "))
nr = float(input("digite um valor real: "))


op1 = (ni2/2) + (ni1 * 2)
op2 = (ni1+nr) * 3
op3 = (nr*nr*nr)

print("Produto do dobro do primeiro numero inteiro com a metade do segundo: ", op1)
print("Soma do triplo da primeira com a terceira: ", op2)
print("O terceiro elevado ao cubo: ", op3)

# 12) Peso ideal
altura = float(input("digite sua altura: "))
peso_ideal = (72.7*altura)-58
print("O peso ideal para sua altura: ",peso_ideal)

# 13) Peso ideal H M
genero = input("Digite 1 para homem e 2 para mulher:  ")


if genero == 1:
    altura_h = float(input("digite o valor da sua altura: "))
    peso_ideal = (72.7*altura_h)-58
    print("O seu peso ideal é:  ", peso_ideal)

else:
    altura_m = float(input("digite o valor da sua altura: "))
    peso_ideal = (62.1*altura_m)-44.47
    print("O seu peso ideal é:  ", peso_ideal)

# 14) Programa para o João papo de pescador
peso = float(
    input("Qual a quantidade de kilos de peixe trouxe hoje seu João? "))
excesso = peso - 50
multa = excesso * 4.00
print('João voce pescou: ', peso, 'kg')
print('João sinto informar mas tem um exedente de: ', excesso, 'kg')
print('Que renderam uma multa no valor de: ', multa, 'R$')

# 15) Relação salárial
valor_h = float(input('Digite o valor que voce ganha por hora: '))
horas_mes = float(input('Digite quantas horas voce trabalha por mes: '))
salario = valor_h * horas_mes
inss = salario * 0.08
ir = salario * 0.11
sindicato = salario * 0.05
salario_liquido = (((salario - inss) - ir) - sindicato)
print('Valor do seu salario bruto: ', salario, 'R$')
print('Valor de desconto para o INSS: ', inss, 'R$')
print('Valor de desconto para o imposto de renda:  ', ir, 'R$')
print('Valor pago para o sindicato:  ', sindicato, 'R$')
print('Salário liquido:  ', salario_liquido, 'R$')
'''
# 16) Programa para suvinil
area = float(input('quantos m² voce precisa pintar:  '))
quantidade_litros_tinta = (area/3)
quantidade_de_latas = 

print(quantidade_litros_tinta)

