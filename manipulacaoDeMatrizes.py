###Manipulação de matrizes

class Matriz(object):

    def cria_matriz(self, num_linhas, num_colunas, valor):
    
        matriz = []
        for i in range(num_linhas):
            #cria a linha i
            linha = []
            for j in range(num_colunas):
                linha.append(valor)
                
            matriz.append(linha)
            
        return matriz 

    def soma_matrizes(self, m1, m2):
        num_lin1 = len(m1)
        num_col1 = len(m1[0])
        tamanho1 = (num_lin1, num_col1)
        
        num_lin2 = len(m2)
        num_col2 = len(m2[0])
        tamanho2 = (num_lin2, num_col2)
        
        if tamanho1 == tamanho2:
            c = self.cria_matriz(num_lin1, num_col1, 0) # self para chamar outra função da mesma classe
            
            for lin in range(num_lin1):
                for col in range(num_col1):
                    c[lin][col] = m1[lin][col] + m2[lin][col]
                    
            return c 
        
        else:
            return False

    def multiplica_matrizes(self,A, B):
    
        num_linhas_A, num_colunas_A = len(A), len(A[0])
        num_linhas_B, num_colunas_B = len(B), len(B[0])
        assert num_colunas_A == num_linhas_B
        C = []
        
        for linha in range(num_linhas_A):
            '''a matriz resultante da multiplicação terá dimensão
            de num_linhas_A X num_colunas_B, os dois primeiros for
            são para criar essas linhas e colunas, com o elemento neutro
            da soma, 0'''
            
            C.append([])
            
            for coluna in range(num_colunas_B):
                C[linha].append(0)
                
                for k in range(num_colunas_A):
                    C[linha][coluna] += A[linha][k]*B[k][coluna]
                    
        return C

    def dimensao_matriz(self, minha_matriz):

    
        tamanho = len(minha_matriz), len(minha_matriz[0])
        
        return tamanho[0], tamanho[1]

    def transposta_matriz(self, matriz):
    
        transposta = []
        for i in range(len(matriz[0])):
            #cria a linha transposta
            linha_transposta = []
            for linha in matriz:
                linha_transposta.append(linha[i])
                
            transposta.append(linha_transposta)
            
        return transposta 

def main():

    s = Matriz() 
    
    print("Teste 1 - cria_matriz")

    num_linhas = 4 
    num_colunas = 4 
    valor = 2

    print(s.cria_matriz(num_linhas, num_colunas, valor)) 
    ##[[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    
    print()
    print("Teste 2 - soma_matrizes")  

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    print(s.soma_matrizes(m1, m2)) 
    ##[[11, 22, 33], [44, 55, 66], [77, 88, 99]]
    
    print()
    print("Teste 3 - multiplica_matrizes")

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]

    print(s.multiplica_matrizes(A, B))
    ##[[22, 28], [49, 64]]
    
    print()
    print("Teste 4 - dimensao_matriz")

    minha_matriz = [[1, 2], [3, 4], [5, 6]]

    print(s.dimensao_matriz(minha_matriz))
    ##(3,2)

    print()
    print("Teste 5 - transposta_matriz")

    matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    print(s.transposta_matriz(matriz))
    ##  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

main()