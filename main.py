import os
exesec = input("Tek Dosya mı Birden fazla dosya mı olsun? 1 veya 2 > ")
if(exesec=="1"):
	import os
	os.system("pip install pyinstaller")
	projeadi = input("Python Dosyasının yolunu belirtiniz > ")
	os.system("pyinstaller --onefile "+projeadi)
elif(exesec=="2"):
	import os
	os.system("pip install pyinstaller")
	projeadi = input("Python Dosyasının yolunu belirtiniz > ")
	os.system("pyinstaller "+projeadi)
else:
	print("Sadece 1 veya 2 yazacaksın")
	os.system("python3 iss.py")
