x = 10
while x:
    print(x)
    x -=1
print('...Fim...')


nota = 0
qtd = 0
total = 0.0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair.: '))
    if nota != -1:
        qtd += 1
        total += nota

print(f'A media da turma é {total / qtd}')