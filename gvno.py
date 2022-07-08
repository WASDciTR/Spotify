import os,time

try:
    import requests_toolbelt
    import requests
    from colorama import *
    from pystyle import Colors, Colorate
    import bs4, psutil
    from zipfile import ZipFile
except ModuleNotFoundError:
    print("Modul Eksik")
    print("Yukleniyor....")
    os.system("pip install requests_toolbelt")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install bs4")
    os.system("pip install psutil")
    os.system("pip install pycryptodome")
    os.system("pip install zipfile")
    print("Yuklendi! Tekrar Ac")
    print("Yuklendi! Tekrar Ac")
    print("Yuklendi! Tekrar Ac")
    print("Yuklendi! Tekrar Ac")
    print("Yuklendi! Tekrar Ac")
    print("Yuklendi! Tekrar Ac")
    time.sleep(1.5)
    exit(0)

os.system("cls")

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

print("")
print("")
print(Fore.MAGENTA+"                     Dinleyici Hesabi:1                                  Artist Hesabi:2")
option = int(input("\n╰──> "))
os.system("cls")
if option == 1:
    os.system("python user.py")
if option == 2:
    os.system("python artist.py")
