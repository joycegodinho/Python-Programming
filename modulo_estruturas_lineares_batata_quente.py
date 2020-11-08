# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:17:07 2020

@author: joyce
"""

## módulo estruturas lineares: Jogo da batata quente

from orientado_estruturas_lineares import Fila

'''
Implementação uma simulação geral do jogo da batata quente. O programa inserirá uma lista 
de nomes e uma constante, chamada "num", a ser usada para a contagem. Retornará o nome da 
última pessoa restante após a contagem repetida por num. 

Para simular o círculo, usaremos uma fila . Suponha que a criança segurando a batata esteja 
na frente da fila. Ao passar a batata, a simulação simplesmente desenfileirará e imediatamente 
enfileiraria a criança, colocando-a no final da linha. Ela então esperará até que todos os 
outros estejam na frente antes que seja sua vez novamente. Após as num operações de 
desenfileiramento / enfileiramento, a criança na frente será removida permanentemente e 
outro ciclo começará.     
'''

def Batata(lista, num):
    
    fila = Fila()
    
    for nome in lista:
        fila.adc(nome)
        
    while fila.tamanho() > 1:
        for n in range(num):
            fila.adc(fila.pop())
            
        fila.pop()
        
    return fila.pop()
            
    
print(Batata(["João","Maria","José","Ana","Bia","Pedro"],7))    
    
    
    
    
    
    
    
    
    
    