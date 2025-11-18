import os
import sys
import time

def hilangkan_teks():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

 

if __name__ == "__main__":
    hilangkan_teks()
    type_effect()
