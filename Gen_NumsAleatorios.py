# -*- coding: utf-8 -*-

#Generador de Números aleatroios
#Grupo 7 - Simulación Digital

import math

#--------------------------------------------LEHMER----------------------------------------------------------------------
class LehmerGenerator:
    def __init__(self, seed, a, m, c):
        self.seed = seed
        self.a = a
        self.m = m
        self.c = c
    
    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed 

#______________________________________________Shift-Resiter______________________________________________________________
class Shift_Register:
    def __init__(self, k, feedback , num_bits):
        self.num_bits = num_bits 
        self.shift_register = feedback[:] # Inicializar el registro de desplazamiento con el estado inicial
        self.feedback = feedback # Definir la retroalimentación
        self.k = k # Definir la longitud del registro de desplazamiento

    def next(self): #Método principal
        sequence = [] 

        for i in range(self.num_bits):
            print("\n---- Iteración", i+1, "de", self.num_bits)
            # Calcular la retroalimentación
            feedback_bit = sum([self.shift_register[j] * self.feedback[j] for j in range(self.k)]) % 2
            print("Formula:", feedback_bit)
            
            # Desplazar el registro de desplazamiento
            self.shift_register = [feedback_bit] + self.shift_register[:-1]
            print("Concatenamos:", feedback_bit, "y obtenemos shift:", self.shift_register)
            
            # Agregar el bit de salida a la secuencia
            sequence.append(self.shift_register[-1])
            print("Secuencia:",sequence)

        return int(''.join([str(bit) for bit in sequence]), 2) #Convertir de binario a decimal
    
#__________________________________________________________Lagged-Fibonacci______________________________________________________
class Lagged_Fibonacci:
    def __init__(self, n, j , k, seeds, m):
        self.j = j 
        self.k = k 
        self.register = seeds 
        self.n = n 
        self.m = m

    def next(self): #Método principal
        sequence = []

        for i in range(self.n): #Tomemos i como k
            print("\nIteración", i+1, "de", self.n)

            # Calcular el índice del número aleatorio
            
            indexA = (i-k) % len(self.register)
            indexB = (i-j) % len(self.register)
                
            print("Ia:", indexA, "Ib:", indexB )
            
            # Calcular el número aleatorio y agregarlo a la secuencia
            random_number = (self.register[indexB] + self.register[indexA]) % (2**self.m)
            print("Número generado:", random_number)
            sequence.append(random_number)
            
            # Actualizar el registro de desplazamiento con el número aleatorio
            self.register[i % len(self.register)] = random_number
            print("Nueva semilla:", self.register)

            


        return sequence
    
#__________________________________________________________MAIN__________________________________________________________________

#--------------------Generador de lehmer
n = 64 #Cantidad

array = n * [0]#Init array

generator = LehmerGenerator(seed=3, a=3, c=0, m=128)
for i in range(n):
    array[i] = generator.next()

#print("Números generados:",array)

#--------------------Shift_Register
f = [1, 0, 0, 1]
n_bits = 9

generator = Shift_Register(k=4, feedback=f, num_bits=n_bits)
#print("\nNúmero generado:",generator.next())

#--------------------Lagged-Fibonacci
seeds = [3, 7, 9, 11]
k = 3 #k<=m
j = 1 #j<k
n = 56
m = 3 

generator = Lagged_Fibonacci(n=n, j=j, k=k, seeds=seeds, m=m)
print("\nSecuencia generado:",generator.next())
