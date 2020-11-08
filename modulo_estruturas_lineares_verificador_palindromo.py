# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:08:40 2020

@author: joyce
"""
# verificador de palindromo

from orientado_estruturas_lineares import Deque

def verificador(string):
    
    deque = Deque()
    
    for l in string:
        deque.adcTras(l)
        
    igual = True
        
    while deque.tamanho() > 1 and igual:
        
        primeira = deque.retiraFrente()
        ultima = deque.retiraTras()
        
        if primeira != ultima:
            igual = False
        
    return igual

print (verificador("lsdkjfskf"))
print (verificador("radar"))
