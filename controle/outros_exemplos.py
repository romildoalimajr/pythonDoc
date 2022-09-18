pessoa = ['Romildo', 'Clara']
adj = ['inteligente', 'sabido']

for p in pessoa:
    for a in adj:
        print(f'{p} é {a}')

for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i, end=' ')
print('')
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print('')
print('---Fim---')