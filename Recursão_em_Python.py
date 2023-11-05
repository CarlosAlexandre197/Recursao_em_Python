'''Recursão em Python
Uma função recursiva em Python é uma função que chama a si mesma. 
Essas funções têm um caso base que interrompe o processo recursivo e
um caso recursivo que continua o processo recursivo fazendo outra chamada recursiva.'''

#Função fatorial recursiva

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
#Função de Fibonacci

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Encontrar uma potência recursivamente

def encontrar_potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * encontrar_potencia(a, b-1)