#!python3

# import pacote.sub.arquivo

#print('Olá Mundo!')
#print('Bem Vindo!')
#import tipos.variaveis
# from tipos import variaveis
#from tipos import basicos
#from tipos import lista
#from tipos import tuplas
#from tipos import conjuntos
#from tipos import dicionarios
#from operadores import unarios
#from operadores import aritmeticos
#from operadores import relacionais
#from operadores import atribuicao
#from operadores import logicos
#from operadores import ternario
#from controle import if_1
#from controle import if_2
#from controle import for_1
#import controle.while_1
#import controle.outros_exemplos

from funcoes import basico

basico.saudacao()
basico.saudacao('Clara', 9)
basico.saudacao('Romildo', 28)
basico.saudacao(idade = 89)

a = basico.soma_e_multi(x = 10, a=2, b=3)
b = basico.soma_e_multi(x = 20, a=3, b=7)

resultado = a + b
print(resultado)



