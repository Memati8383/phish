import sys
from ferit import text

# Animasyonu silip sadece ferit yazısını ekrana yazdırma
def temizle_ve_yazdir(text):
    print('\033[K' + text, end='')
    sys.stdout.flush()
