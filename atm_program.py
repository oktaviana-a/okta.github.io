import random
from datetime import date
from datetime import datetime
from customer import Customer

saldo = 10000
today = date.today()
now = datetime.now()

class Customer(Customer):
	"""docstring for Customer"""
	def __init__(self, id='', custPin='', custBalance=''):
		super().__init__(id, custPin, custBalance)

	def info (self):
		return self.id + str(self.custPin) +str(self.custBalance)



coba_pin = 0
while True:
	id = int(input("Masukkan Nomor Pin anda: "))
	if id == 1234:
		break

	print ("Silahkan masukkan nomor pin anda lagi")	
	coba_pin += 1

	if coba_pin ==3:
		print("Silahkan masukkans kartu anda kembali")
		exit()

while True:
	print("")
	print("")
	print("=========SELAMAT DATANG DI ATM *SUN AND MOON*=========")
	print("")
	print("")
	menu1 = Customer (" Cek saldo")
	menu2 = Customer (" Debet")  
	menu3 = Customer (" Deposit")
	menu4 = Customer (" Ganti Pin")
	menu5 = Customer (" Keluar")

	menus= [menu1, menu2, menu3, menu4, menu5]

	#print("Customer")
	index = 1
	for customer in menus:
		print(str(index)+'.'+customer.info())
		index += 1

	print("")
	print("")
	#exit()
	pilih = int(input('Masukkan Pilihan kamu: '))
	#memilih = menus[pilih]
	#saldo = memilih.saldo
	#debet = memilih.debet


	if pilih == 1:
		print ("Saldo kamu: " + str(saldo) )

	elif pilih == 2:

		print("Saldo kamu sebesar Rp " + str(saldo))
		pengambilan= int(input("Masukkan jumlah pengambilan: "))
		count = int(pengambilan)
		#hasil = memilih.debet 

		if saldo >= count:
			print("Silahkan ambil uang kamu Rp " + str(count))
			saldo -= count
			print ("Jumlah saldo kamu sekarang : " + str(saldo))

		else:
			print ("saldo tidak mencukupi")
			
	elif pilih == 3:
		print("Saldo kamu sebesar Rp " + str(saldo))
		simpan= int(input("Masukkan jumlah penyetoran: "))
		count = int(simpan) 

		if saldo >= count:
			saldo += count
			print ("Jumlah saldo kamu sekarang : " + str(saldo))

	elif pilih == 4:
		 pin_baru = input('Masukkan Pin Baru ')
		 print ("Pin lama kamu adalah:  " +str(id))
		 if pin_baru == pin_baru:
		 	id = int(pin_baru)
		 	print ("Pin Baru kamu sekarang adalah: " +str(pin_baru))
		 else:
		 	print("Maaf kamu tidak punya akses")

	elif pilih == 5:
		cek = input("Apakah kamu yakin akan keluar?, y/n: ")
		if cek == "y":
			print("")
			print("")
			print("Transaksi kamu sudah selesai")
			print("")
			print("")
			print("Nomor Transaksi: ", random.randint (100000, 1000000))
			hari_ini = today.strftime("%B %d, %Y")
			print("Tanggal Transaksi: ", hari_ini)
			jam = now.strftime("%H:%M:%S")
			print("Pukul: ", jam, "WIB")
			print("")
			print("Saldo kamu saat ini Rp. " + str(saldo))
			print("")
			print("")
			print("Terima kasih sudah menggunakan layanan ATM *SUN & MOON* ")
			print("")
			print("")
			print("Tetap jaga kesehatan, jaga jarak aman dan selalu gunakan masker")
		
			exit()

