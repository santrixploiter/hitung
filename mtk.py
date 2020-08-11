#/bin/python
#Belajar doank :v
#by Rakha
import os
os.system('clear')
import pyfiglet     
import time
print ("\33[36;1m")
ascii_banner = pyfiglet.figlet_format("Aritmatika")
print (ascii_banner)
print ("\tCoded by : Yonanda")
print ("\tTeam : SantriXploiter")
print ("\33[37;1m")
print ("[1] penjumlahan")
print ("[2] pengurangan")
print ("[3] perkalian")
print ("[4] pembagian")
print ("\33[36;1m")
pilih = input("pilih : ")
if pilih == "1":
  a = int(input("angka pertama : "))
  b = int(input("angka kedua : "))
  time.sleep(1)
  hasil = a + b
  print ("\33[37;1mhasil dari", a ,"ditambah", b ,"adalah","\33[36;1m", hasil)
  print ("\33[37;1m")
elif pilih == "2":
  a = int(input("angka pertama : "))
  b = int(input("angka kedua : "))
  time.sleep(1)
  hasil = a - b
  print ("\33[37;1mhasil dari", a ,"dikurangi", b ,"adalah","\33[36;1m", hasil)
  print ("\33[37;1m")
elif pilih == "3":
  a = int(input("angka pertama : "))
  b = int(input("angka kedua : "))
  time.sleep(1)
  hasil = a * b
  print ("\33[37;1mhasil dari", a ,"dikali", b ,"adalah","\33[36;1m", hasil)
  print ("\33[37;1m")
elif pilih == "4":                                                                        
  a = int(input("angka pertama : "))
  b = int(input("angka kedua : "))                                                        
  time.sleep(1)
  hasil = a / b
  print ("\33[37;1mhasil dari", a ,"dibagi", b ,"adalah","\33[36;1m", hasil)
  print ("\33[37;1m")