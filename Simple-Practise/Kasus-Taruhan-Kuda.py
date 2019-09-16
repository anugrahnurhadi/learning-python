#Oleh Anugrah Noer Hadi
#Gunakam Pythom 2.7
#Roy, Ananto, dan Abi berada di perjalanan ke padang gurun di Maroko. Perjalanan termasuk naik onta. Pemandu mereka mengundang mereka untuk melihat balapan onta di malam hari. Onta mereka juga akan berpartisipasi dan adalah adat untuk bertaruh pada hasil balapan.
#Salah satu taruhan yang paling menarik melibatkan menebak urutan lengkap di mana unta akan menyelesaikan lomba. Taruhan ini menawarkan hadiah paling besar, karena salah satu yang paling sulit.
 
#Roy, Ananto, dan Abi telah melakukan taruhan mereka, tetapi perlombaan tidak akan mulai sampai satu jam dari sekarang sehingga mereka mulai bosan. Mereka mulai bertanya-tanya berapa banyak pasangan unta mereka telah dimasukkan ke dalam urutan yang sama. Jika onta C ditempatkan sebelum onta D pada taruhan Roy, Ananto, dan Abi, itu berarti bahwa semua tiga dari mereka menempatkan C dan D dalam urutan yang sama. Apakah Anda dapat membantu mereka untuk menghitung jumlah pasangan onta ini?
Input
#jumlah_onta, integer antara 2 sampai 100.
#taruhan_roy, array of integer sejumlah jumlah_onta. Setiap nomor mewakili onta
#tertentu, setiap nomor hanya muncul sekali.
#taruhan_ananto, sama seperti taruhan_roy,
#taruhan_abi, sama seperti taruhan_roy.

#Output: Jumlah pasangan onta yang muncul dalam urutan yang sama diketika taruhan.

#Contoh:
#Inputan 1:
#jumlah_onta: 3
#taruhan_roy: 3, 2, 1
#taruhan_ananto: 1, 2, 3
#taruhan_abi: 1, 2, 3
#Output 1: 0
#Inputan 2:
#jumlah_onta: 4
#taruhan_roy: 2, 3, 1, 4
#taruhan_ananto: 2, 1, 4, 3
#taruhan_abi: 2, 4, 3, 1
#Output 2: 3




#MEMASUKAN JUMLAH ONTA INTEGER DARI 2 - 100
jumlah_onta=1
while ((jumlah_onta<2) or (jumlah_onta>100)):
	jumlah_onta=input("masukan jumlah onta (2-100) : ")


#MASUKAN TARUHAN TIAP ORANG DENGAN KETENTUAN ANGKA SATU SAMPAI DENGAN JUMLAH ONTA DAN DALAM 1  SUSUNAN TARUHAN TIDAK BOLEH ADA ANGKA YANG SAMA
#TARUHAN ROY
sama=2
taruhan_roy=[0] * jumlah_onta
while ((sum(1 for x in taruhan_roy if x<1)>=1) or (sum(1 for x in taruhan_roy if x>jumlah_onta)>=1) or (len(taruhan_roy)!=jumlah_onta) or (same>1)):
	taruhan_roy=input("masukan taruhan roy: ")
	for n in taruhan_roy:
		same=taruhan_roy.count(n)
		if same>1:
			sama=same
#TARUHAN ANANTO	
sama=2
taruhan_ananto=[0] * jumlah_onta
while ((sum(1 for x in taruhan_ananto if x<1)>=1) or (sum(1 for x in taruhan_ananto if x>jumlah_onta)>=1) or (len(taruhan_ananto)!=jumlah_onta) or (same>1)):
	taruhan_ananto=input("masukan taruhan ananto: ")
	for n in taruhan_ananto:
		same=taruhan_ananto.count(n)
		if same>1:
			sama=same

#TARUHAN ABI
sama=2
taruhan_abi=[0] * jumlah_onta
while ((sum(1 for x in taruhan_abi if x<1)>=1) or (sum(1 for x in taruhan_abi if x>jumlah_onta)>=1) or (len(taruhan_abi)!=jumlah_onta) or (same>1)):
	taruhan_abi=input("masukan taruhan abi: ")
	for n in taruhan_abi:
		same=taruhan_abi.count(n)
		if same>1:
			same=sama

#MENGHITUNG JUMLAH PASANGAN ONTA YANG MUNCUL DALAM URUTAN YANG SAMA 
urutan_sama=0
for i in range(0,jumlah_onta):
	if (taruhan_roy[i]==taruhan_ananto[i]) and (taruhan_roy[i]==taruhan_abi[i]):
		urutan_sama=urutan_sama+1

print "Jumlah Pasangan Onta yang muncul dalam urutan yang sama :  ", urutan_sama
	
