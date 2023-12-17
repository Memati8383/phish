import sys, time
from colorama import Fore, Style

# İlk animasyon
def renkli_animasyon():
    symbols = [Fore.RED + "█" + Fore.RESET, Fore.YELLOW + "█" + Fore.RESET, Fore.GREEN + "█" + Fore.RESET, Fore.BLUE + "█" + Fore.RESET]
    
    for i in range(1, 41):
        sys.stdout.write('\r')
        sys.stdout.write(''.join([symbols[(i + j) % len(symbols)] for j in range(40)]))
        sys.stdout.flush()
        time.sleep(0.2)
