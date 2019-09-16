#ANUGRAH NOER HADI
#Setiap tahun, perusahaan mengharuskan karyawannya untuk mengganti password. Peraturan yang dibuat oleh system admin sangat ketat, dan setiap password harus mengikuti aturan berikut: 
#1.Hanya boleh mengandung huruf dan angka. 
#2.Harus antara huruf A dan B (inclusive). 
#3.Harus mengandung setidaknya 1 huruf kecil, 1 huruf besar, dan 1 angka. 
#4.idak boleh mengandung kata-kata yang diblacklist. 
#Kata yang dianggap blacklist dianggap ada di password apabila tampil sebagai substring , apabila karakter yang berurutan (terlepas itu huruf besar/ kecil). Sebagai contoh sepulsa adalah substring dari SePuLsA, 2017sepulsa2017  atau SEPULSA17. Tetapi bukan substring dari STIP atau sepu171sa. 
#Tambahan, untuk tujuan menghindari blacklist, tidak bisa menggunakan 133t . Terutama beberapa angka bisa diterjemahkan sebagai huruf, seperti 1 ('i'), 3 ('e'), 5 ('s'), 0 ('o'), dan 7 ('t'). Jadi dengan contoh di atas, 54puls4 akan dibaca sebagai sepulsa dan abcl33tdef mengandung kata l33t. 
#Dirimu tidak bisa berhenti berpikir, dengan semua peraturan tersebut, ada berapa banyak kemungkinan password di sana.  

#Task
#Dengan daftar blacklist yang mengandung N kata-kata dan 2 angka A dan B , tugasmu adalah untuk menghitung berapa banyak password yang valid dengan aturan: hanya terdiri dari huruf dan angka;  panjang antara A dan B (inclusive); setidaknya 1 huruf kecil, 1 huruf besar, dan 1 angka; tidak ada kata-kata yang ada di dalam daftar blacklist. Karena hasilnya bisa sangat besar, hitung dengan modulo 1 000 003. 



#Input 
#Baris pertama berisi 2 angka,  A dan B, untuk menentukan berapa panjang minimal dan maksimal dari passwordnya. Baris kedua berisi angka N, menentukan berapa banyak daftar isi di blacklist. Baris selanjutnya sebanyak N masing-masing berisi kata W, menandakan kata-kata yang di blacklist. Kata-kata ini hanya berupa huruf kecil. 

#Constraint
#3 ≤ A ≤ B ≤ 20                          	Panjang password  
#0 ≤ N ≤ 50                                	Banyak kata dalam blacklist  
#1 ≤ panjang (Wi) ≤ 20            	Ukuran untuk setiap kata dalam blacklist  

#Output
#Hasil harus berupa 1 baris angka yang merupakan banyaknya jumlah password yang mungkin di modulo 1 000 003. Password yang valid adalah password yang mengikuti semua syarat.  


#MEMASUKKAN PANJANG MINIMUM DENGAN BATAS 3 SAMPAI 20
A=1
while((A<3) or (A>20)):
	A=input("masukkan panjang minimum password : ")

#MEMASTIKAN PANJANG MAKSIMUM LEBIH DARI NILAI MINIMUM SAMPAI 20
B=1
while ((B<A) or (B>20)):
	B=input("masukan panjang maksimum password : ")

#MEMASUKAN BANYAK KATA DALAM BLACKLIST
N=0
while((N<1) or (N>50)):
	N=input("Banyak kata dalam Blacklist : ")

#MEMASUKKAN KATA DALAM BLACKLIST DENGAN BATAS PANJANG STRING 1 - 20
W=['']*N
for i in range(0,N):	
	while((len(W[i])<1) or (len(W[i])>20)):
		W[i]=raw_input()
		if (len(W[i])<1) or (len(W[i])>20):
			print("Kata-kata blacklist terlalu panjang atau kosong")

#CONTOH PASSWORD			
password='babangtamvan!','1k3h1k3H','J4J4n9tokEK','up','123','seGO'

salah=0
for pas in password:
#MEMFILTER PASWORD YANG SESUAI DENGAN KRITERIA

	#BAGI YANG SESUAI AKAN DILAKUKAN FILTER LEBIH LANJUT
	if (len(pas)<B) and (len(pas)>A): 
		digit=0
		upper=0
		lower=0

		#MELAKUKAN FILTER UNTUK KRITERIA MINIMAL 1 HURUF BESAR, 1 HURUF KECIL, 1 ANGKA, DAN HANYA TERMASUK ANGKA DAN HURUF

		for i in range(0,len(pas)):
			if pas[i].isdigit()==True:
				digit=digit+1
			elif pas[i].isupper()==True:
				upper=upper+1
			elif pas[i].islower()==True:
				lower=lower+1

		#YANG TIDAK SESUAI KRITERIA AKAN DIANGGAP SALAH
		if (pas.isalnum()==False) or (upper==0) or (lower==0) or (digit==0):
			salah=salah+1
			
		#MELAKUKAN FILTRASI YANG TERKENA BLACKLIS
		else:
			#mENGUBAH UPPERCASE JADI LOWERCASE
			pas=pas.lower()
			#MENGUBAH BEBERAPA ANGKA YANG MIRIP DENGAN HURUF
			pas=pas.replace('3','e')
			pas=pas.replace('1','i')
			pas=pas.replace('5','s')
			pas=pas.replace('0','o')
			pas=pas.replace('7','t')

			#MEMFILTER APAKAH PASSOWR TERKENA KATA-KATA BLACKLIST
			#CATAT : 1 PASSWORD BISA SAJA TERKENA DUA KATA BLACKLIST
			for bl in W:
				kenabl=0
				if pas.find(bl)!=(-1):
					kenabl=kenabl+1
			
			if kenabl>0:
				salah=salah+1
					

	#YANG TIDAK SESUAI KRITERIA DIHITUNG SALAH
	else:
		salah=salah+1
		


#MENGHITUNG MODULUS
modsalah=salah%1000003
print(modsalah)
