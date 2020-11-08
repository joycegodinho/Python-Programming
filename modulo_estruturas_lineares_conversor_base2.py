# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:47:29 2020

@author: joyce
"""


#### solução recursiva como módulo do Estruturas Lineares

#Convertendo um Inteiro para String em Qualquer Base



from orientado_estruturas_lineares import Pilha

rPilha = Pilha() #os itens são adicionados e removidos apenas na frente

def paraString(n, base):
    
    convertString = "0123456789ABCDEF"
    
    while n > 0:
        
        if n < base:
            rPilha.push(convertString[n])
        else:
            rPilha.push(convertString[n % base]) ### adiciona o resto da divisão à pilha
            
        n = n // base # devolve pra o loop a parte inteira da divisão
        
    string_novo = ""
        
    while not rPilha.vazia():
        string_novo = string_novo + str(rPilha.pop()) #pop()remove o item superior da pilha
            
    return string_novo
    
print(paraString(1453,16))