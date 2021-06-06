anonim = {}
anonim['baik'] = 'buruk'
anonim['siang'] = 'malam'
anonim['naik'] = 'turun'
anonim['tinggi'] = 'rendah'

print(anonim)
print(anonim['tinggi'])
print(anonim['siang'])


data_laundry = {
    'hari_ini' : '2021-06-06',
    'customer' : [
        {'nama' : 'budi', 'jenis_pakaian' : 'kemeja, kaos'},
        {'nama' : 'andi', 'jenis_pakaian' :'celana kain, celana levis'},
        {'nama' : 'indra', 'jenis_pakaian': 'singlet, kaos kaki'},
        {'nama' : 'gading', 'jenis_pakaian' :'cd, tas'},
        {'nama' : 'alam', 'jenis_pakaian' : 'seragam sekolah'},
        {'nama' : 'yetra','jenis_pakaian': 'kaos futsal'},
        {'nama' : 'basu', 'jenis_pakaian': 'seragam pencak silat'},
    ]
}
print(f"kerjaan hari ini {data_laundry['customer'][3]}")
print(f"pelanggan dengan nama {data_laundry['customer'][2]}")
print(f"pakaian yang cepat kering adalah : {data_laundry['customer'][2]['jenis_pakaian']}")

