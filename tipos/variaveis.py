
a = 3
b = 4.4

print( a + b )

texto = 'Sua idade é...'
idade = 23

#print(texto + str(idade))
print(f'{texto} {idade}')

print(3 * 'bom dia ')

saudacao = 'boa noite '

print(5 * saudacao)

PI = 3.14
raio = float(input('Informe o raio da circuferência? '))

#area = PI * raio * raio
area = PI * pow(raio, 2)
print(f'A área da circuferencia é de {area} m2.')