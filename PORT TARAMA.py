#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port tarama aracına hoş geldin :)

1) Hızlı tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi
""")

islemno = raw_input("İşlem Numarasını Giriniz: ")

if(islemno=="1"):
    hedefip = raw_input("Hedef Ip Giriniz: ")
    os.system("nmap"+ hedefip)
elif(islemno=="2"):
    hedefip = raw_input("Hedef Ip Giriniz: ")
    os.system("nmap -sS -sV "+ hedefip)
elif(islemno=="3"):
    hedefip = raw_input("Hedef Ip Giriniz: ")
    os.system("nmap -0 "+ hedefip)
else: print("Hatalı Seçim Yaptınız Bay xxx")
