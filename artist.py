from follow_artist import spotify
import threading, os, time
import time
import threading, os, time
import time
import requests_toolbelt
import requests
from colorama import *
from pystyle import Colors, Colorate


print(Colorate.Horizontal(Colors.blue_to_purple, """ 
                                                              )     )   
                                            (              ( /(  ( /(   
                                            )\ )    (   (  )\()) )\())  
                                           (()/(    )\  )\((_)\ ((_)\   
                                            /(_))_ ((_)((_)_((_)  ((_)  
                                           (_)) __|\ \ / /| \| | / _ \  
                                             | (_ | \ V / | .` || (_) | 
                                              \___|  \_/  |_|\_| \___/   
                                                                    """, 1))
print("\n")
print("\n")
time.sleep(1)
lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input("Link: "))
threads = int(input("\nHız (1-50): "))

def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nproxies.txt dosyası bulunamadı")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nproxy.txt dosyasına proxy yüklenmedi")
            time.sleep(10)
            os._exit(0)

print("\n[1] Proxy Kullan\n[2] Proxy Kullanma")
option = int(input("\n> "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print("Takipçi Gönderildi {}".format(counter))
    else:
        safe_print(f"Hata {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0
