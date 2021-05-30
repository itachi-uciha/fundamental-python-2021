print('\ntipe data skalar => tipe data sederhana')
anak1 = 'budi'
anak2 = 'windy'
anak3 = 'ningsih'
anak4 = 'wo'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['budi', 'windy', 'ningsih', 'wo']
print(anak)
anak.append('limo')
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nSapa semua anak: cara kompleks')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')