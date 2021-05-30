"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus

"""

kamus_ind_eng = {}
kamus_ind_eng['anak'] = 'child'
kamus_ind_eng['istri'] = 'wife'
kamus_ind_eng['ayah'] = 'father'
kamus_ind_eng['ibu'] = 'mother'


print(kamus_ind_eng)
print(kamus_ind_eng['istri'])
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['ibu'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-05-30',
    'driver_list': [
        {'nama':'budi', 'jarak': 10},
        {'nama':'windy', 'jarak': 30},
        {'nama':'ningsih', 'jarak': 100},
        {'nama':'wo', 'jarak': 1000},
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
