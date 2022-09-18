lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuuuuuu'

print(status)

print(f'O status é {status}')