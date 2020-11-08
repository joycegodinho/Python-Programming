import string #usado para contar as maiusculas

#Manipulação de strings e lista de strings

class String(object):

    def separa_letras(self, wordlist):

        
        letterlist = []

        for aword in wordlist:
            for aletter in aword:
                if aletter not in letterlist:
                    letterlist.append(aletter)
        return letterlist

    def inverte_lista(self, lista):
        tam = len(lista) - 1
        inversa = []
        while tam >= 0:
            inversa.append(lista[tam])
            tam = tam - 1
        return inversa

    def retira_espacos(self,string):
        pos = 0
        string1 = ""
        while pos < len(string):
            if string[pos] != " ":
                string1 = string1 + string[pos]
            pos = pos + 1
        return string1  

    def mostra_maiusculas(self, frase):
    
        m = ""
        
        for j in frase:
            if j in string.ascii_uppercase:
                m = m + j
        return m

    def menor_nome(self,nomes):
    
        menor = ""
        menor_tamanho = 100
        
        for i in nomes:
            i = i.lstrip()   #The lstrip() method removes any leading characters (space is the default leading character to remove)
            i = i.rstrip()   #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
            
            tamanho = len(i)
            
            if tamanho < menor_tamanho:
                menor_tamanho = tamanho
                menor = i
                
        return menor.capitalize()

    def conta_letras(self, frase, contar="vogais"):
    
        frase = frase.lower()
        vog = 'aeiou'
        cons = 'bcdfghjklmnpqrstvxzyw'
           
        if contar == "vogais":
            return sum(frase.count(i) for i in vog)
        else:
            return sum(frase.count(j) for j in cons) 

    def verifica_anagrama (self, s1, s2):
        
        lista1 = list(s1)
        lista2 = list(s2)
        
        lista1.sort()
        lista2.sort()

        pos = 0
        iguais = True
        
        while pos < len(s1) and iguais:
            if lista1[pos] == lista2[pos]:
                pos = pos + 1
            
            else:
                iguais = False
        
        return iguais
    
    def verificador_palindromo(self, st):
    
        st = st.replace(" ", "") #retira os espaços
        a = 0
        b = len (st) - 1 
        
        igual = True
        
        while b > 1 and igual:
            if st[a] != st[b]:
                igual = False
            else:
                a = a + 1
                b = b - 1
        return igual

    def inverte_string(self,stn):
    
        stn = list(stn)
        tam = len(stn) - 1
        resp = ""
        
        while tam >= 0:
            resp = resp + stn[tam]
            tam = tam - 1

        return resp
    

def main():

    s = String() 
    
    print("Teste 1 - separa_letras - (e remove repetidas)")

    wordlist = ['cat','dog','rabbit']
    print(s.separa_letras(wordlist)) 
    ## ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

    print()
    print("Teste 2 - inverte_lista")

    lista = ["margarida", "rosa", "tulipa", "cravo"]
    print(s.inverte_lista(lista)) 
    ## ['cravo', 'tulipa', 'rosa', 'margarida']

    print()
    print("Teste 3 - retira_espacos")

    string = "E UM TESTE"
    print(s.retira_espacos(string)) 
    ## EUMTESTE

    print()
    print("Teste 4 - mostra_maiusculas")

    frase = 'Programamos em python 2?'
    print(s.mostra_maiusculas(frase)) 
    ## P

    print()
    print("Teste 5 - menor_nome")

    nomes = ['maria', ' jose  ', '  PAULO', 'Catarina  ']
    print(s.menor_nome(nomes)) 
    ## Jose

    print()
    print("Teste 6 - conta_letras")

    frase = 'programamos em python'
    contar = 'consoantes'
    print(s.conta_letras(frase, contar)) 
    ## 13

    print()
    print("Teste 7 - verifica_anagrama")

    s1 = 'abcde'
    s2 = 'edcba'
    print(s.verifica_anagrama (s1, s2)) 
    ## True

    print()
    print("Teste 7 - verificador_palindromo")

    st = "madam i m adam"
    print(s.verificador_palindromo(st)) 
    ## True

    print()
    print("Teste 8 - inverte_string")

    stn = "hello"
    print(s.inverte_string(stn)) 
    ## True

main()