angka1=int (input('masukan angka pertama:'))
angka2=int (input('masukan angka kedua:'))
print('operator : 1.penjumlahan \n2. 2.pengurangan'
'\n3.perkalian \n4. pembagian')
pilih=int(input('pilih operator :'))
if pilih == 1:
    tambah = angka1+angka2 
    print('hasilnya adalah ',tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('hasilnya adalah', kurang)
elif pilih == 3:
    kali = angka1*angka2
    print('hasilnya adalah', kali)
elif pilih == 4:
    bagi = angka1/angka2
    print('hasilnya adalah', bagi)
else :
    print('operator yang anda masukan tidak ada')