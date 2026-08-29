while True:
	suhu = int(input("Masukkan suhu : "))
	
	if suhu < 25 :
		status = "Dingin"
	elif suhu > 30 :
		status = "Panas"
	else :
		status = "Normal"
		
	print("Kondisi ruangan :", status)
	print()
print()