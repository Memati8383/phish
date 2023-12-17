import os

def modul_indir():
    os.system("clear")
    
    # Modüllerin kontrolü
    moduller = ["python", "pip", "git"]
    for modul in moduller:
        kontrol_komutu = f"which {modul}"
        kontrol_sonucu = os.system(kontrol_komutu)
        
        if kontrol_sonucu != 0:
            print(f"{modul} modülü bulunamadı. Yükleniyor...")
            os.system(f"pkg install {modul}")
    
    # colorama modülünün kontrolü
    colorama_kontrol = os.system("pip show colorama")
    if colorama_kontrol != 0:
        print("colorama modülü bulunamadı. Yükleniyor...")
        os.system("pip install colorama")
    
    # requests modülünün kontrolü
    requests_kontrol = os.system("pip show requests")
    if requests_kontrol != 0:
        print("requests modülü bulunamadı. Yükleniyor...")
        os.system("pip install requests")
    
    os.system("chmod +x main.py")
    os.system("clear")




#import os

#def modul_indir():
#  os.system("clear")
#  os.system("apt update && apt upgrade")
#  os.system("pkg install python")
#  os.system("pkg install pip")
#  os.system("pkg install git")
#  os.system("pip install colorama")
#  os.system("pip install requests")
#  os.system("chmod +x main.py")
#  os.system("clear")
