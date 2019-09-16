#ANUGRAH NOER HADI
#Task
#Buat fungsi munculSekali(string) sesuai dengan deskripsi di bawah.

#Input
#Satu variable string berisi kumpulan angka.

#Output
#Array berisi angka yang hanya muncul 1 kali pada input.


#MASUKKAN STRING ANGKA
a=raw_input("Masukkan string angka : ")

#MENGUBAH STRING KE ARRAY
a=map(int,a)

bedasendiri=[]

#MENCARI ARRAY YANG HANYA KELUAR SEKALI
for i in range(min(a),max(a)+1):
	idx=a.count(i)
	if idx==1:
		bedasendiri.append(i)

#PRINT ARRAY YANG HANYA KELUAR SEKALI
print "Array yang hanya keluar sekali : ",bedasendiri




