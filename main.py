import requests, os, json, sys, time
from colorama import Fore, Style

os.system("clear")
os.system("chmod +x main.py")
os.system("pip install requests")
os.system("clear")

def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    for i in range(1, 16):  # Adjusted the range for a smoother animation
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)  # Adjusted the sleep time for a faster animation

def renkli_animasyon():
    symbols = [Fore.RED + "█" + Fore.RESET, Fore.YELLOW + "█" + Fore.RESET, Fore.GREEN + "█" + Fore.RESET, Fore.BLUE + "█" + Fore.RESET]
    
    for i in range(1, 41):
        sys.stdout.write('\r')
        sys.stdout.write(''.join([symbols[(i + j) % len(symbols)] for j in range(40)]))
        sys.stdout.flush()
        time.sleep(0.2)

def temizle_ve_yazdir(text):
    print('\033[K' + text, end='')  # Metni temizle ve yazdır
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

print(renkli_text)
renkli_animasyon()
os.system("clear")
temizle_ve_yazdir(renkli_text)
