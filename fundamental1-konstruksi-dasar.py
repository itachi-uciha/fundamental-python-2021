# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL : eksekusi berurutan
print('Hello World')
print('by Budi')
print('tanggal 30 Mei 2021')
print('-' * 10)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('jalan lain')

#PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1):
    print(f'Halo anak #{index_anak}')
