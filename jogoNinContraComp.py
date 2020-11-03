"""
Created on Wed Apr 15 06:03:10 2020

@author: Joyce
"""


def usuario_escolhe_jogada(n,m):
    
    retiradas = 0
    
    while retiradas == 0:
        retiradas = int(input('Quantas peças você vai retirar? '))
        
        if retiradas > n or retiradas < 1 or retiradas > m:
            print('Ops! Jogada inválida')
            retiradas = 0
    
    return retiradas
        
    

def computador_escolhe_jogada(n,m):

    if m >= n:
        numero = n
    else:
        numero = n%(m+1)

    return numero

def campeonato():
    
    rodada = 1
    
    while rodada <= 3:
        print()
        print('****Rodada', rodada, '****')
        print()
        partida()
        rodada = rodada + 1
    
    print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')




def partida():
           
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
    
        x = n%(m + 1)    
        
        computador_joga = False
    
        if x == 0:
            print('Você começa!')
           
        else:
            print('Computador começa!')
            computador_joga = True
            
    
        while n > 0:
            if computador_joga:
                numero = computador_escolhe_jogada(n,m)
                n = n - numero
                print('O computador tirou',numero)
                
                if n == 1:
                    print('Agora resta apenas uma peça no tabuleiro.')
                else:
                    if n == 0:
                        print('Fim do jogo! O computador ganhou!')
                    else:
                        print('Agora restam', n , 'peças no tabuleiro.')
                    
                
                computador_joga = False
            else:
                retiradas = usuario_escolhe_jogada(n,m)
                n = n - retiradas
                print('Você tirou',retiradas)
                
                if n == 1:
                    print('Agora resta apenas uma peça no tabuleiro.')
                else:
                    
                    print('Agora restam', n , 'peças no tabuleiro.')
                
                computador_joga = True

######definições de campeonato##########
    
print('Bem-vindo ao jogo do NIM! Escolha: ')
print('1 - para jogar uma partida isolada')
tipo = int(input('2 - para jogar um campeonato '))
    
if tipo == 2:
    print()
    print('Você escolheu campeonato!')  
    print()
    campeonato()
        
else:
    if tipo == 1:
        print()
        partida()
    
    
###############################    
