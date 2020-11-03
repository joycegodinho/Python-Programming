"""
Created on Fri Apr 17 11:14:58 2020

@author: Joyce
"""

#designar jogador 

jogador= 1 

#definir o estado inicial (número de peças)

estado = 21 #definir como input

print('O número de peças é agora', estado)

while True:   
    
    #aceitar uma jogada valida
    
    print ('Jogador', jogador)
    
    while True:
    
        jogada = int(input('Qual a sua jogada? '))
    
        if jogada in [1,2,3]: 
            break
        print('Jogada não permitida')
    
    #atualizar o estado
    
    estado = estado - jogada
    
    print ('O número de peças é agora', estado)
    #checar o placar
    
    if estado==1:
        print('O jogador',jogador, 'venceu.')
        break
    
    #mudar de jogador (voltar para a linha de jogada válida, possível atrave´s do while)
    
    if jogador==1:
        jogador = 2
    else:
        jogador=1
        
print ('O jogo acabou')
