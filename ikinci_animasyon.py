import sys, time

# İkinci animasyon
def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    for i in range(1, 16):
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)
