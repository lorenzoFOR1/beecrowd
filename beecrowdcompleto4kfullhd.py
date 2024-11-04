#coding: utf-8

#beecrowd 1001
'''
import math as mt

A = int(input())
B = int(input())
X = A + B
print("X =", X)
'''
#beecrowd 1002
'''
import math as mt

R = int(float(input()))
Pi = 3.1415
A =  Pi*(R*R)
print("A=", A)
'''
#beecrowd 1003
'''
import math as mt

A = int(float(input()))
B = int(float(input()))
SOMA = A+B
print(f"SOMA =", SOMA)
'''
#beecrowd 1004
'''
import math as mt

A = int(input())
B = int(input())
PROD = A*B
print(f"PROD =", PROD)
'''
#beecrowd 1005
'''
notaa = float(input())
notab = float(input())

peso1 = 3.5
peso2 = 7.5

media_ponderada = (notaa*3.5+notab*7.5)/(3.5+7.5)
saida = "MEDIA ={media_ponderada:.5f}".format(media_ponderada)
print(saida)
'''
#problema 1009 
'''
raio = float(input())
pi = 3.14159
formulavolume = (4/3)* pi * (raio*raio*raio)
print("VOLUME = {0:.3f}".format(formulavolume))
'''
#problema 1010
'''
valores = input().split(' ')
codigo1 = int(valores[0])
quantidade1 = int(valores[1])
valor1 = float(valores[2])

valores = input().split(' ')
codigo2 = int(valores[0])
quantidade2 = int(valores[1])
valor2 = float(valores[2])

total = quantidade1 * valor1 + quantidade2 * valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")
'''