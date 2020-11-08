# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:17:56 2020

@author: joyce
"""

#### Conversor de base

from orientado_estruturas_lineares import Pilha

def divide_por_2(decimal): #Conversão de decimal em binário
        
        pilha_binaria = Pilha()
        
        while decimal > 0:
            
            binario = decimal % 2
            pilha_binaria.push(binario)
            decimal = decimal//2
            
        string_binario = ""
        
        while not pilha_binaria.vazia():
            string_binario = string_binario + str(pilha_binaria.pop())
            
        return string_binario
    
def conversor_de_base(decimal, base): #Conversão para qualquer base
        
        pilha_nova = Pilha()
        
        while decimal > 0:
            
            resto = decimal % base
            pilha_nova.push(resto)
            decimal = decimal//base
            
        string_novo = ""
        
        while not pilha_nova.vazia():
            string_novo = string_novo + str(pilha_nova.pop())
            
        return string_novo
    
## testes    
    
print(divide_por_2(233))
print(conversor_de_base(233,2))
print(conversor_de_base(25,16))