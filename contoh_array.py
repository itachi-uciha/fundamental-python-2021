makanan_favorit = ['mie goreng','capjay','martabak','sate']
print(makanan_favorit)
makanan_favorit.append('soto')
print(makanan_favorit)
print(makanan_favorit[2])



print(f'saya sedang makan {makanan_favorit[0]}')

for m in makanan_favorit :
    print(f'makanan terfavorit {m}')

for m in range(0, len(makanan_favorit)):
    print(f'{m+1} enak sekali {makanan_favorit[m]}')