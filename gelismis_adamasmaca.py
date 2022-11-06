import random
import time
kelimeler=random.choice(["kuş","kedi","köpek","balık","yarasa","ayı","arı","kaplumbağa","maymun"])
hak=5

while True:
    tahmin=input("tahmin: ")
    if tahmin==kelimeler:
        print("tebrikler oyunu kazandınız doğru tahmin")
        break
    if kelimeler!=tahmin:
        print("yanlış tahmin")
        print("  --------  ")
        time.sleep(0.2)
        print("     O      ")
        time.sleep(0.2)
        print("     |      ")
        hak-=1
        tahmin = input("tahmin giriniz: ")
    else:
        print("  --------  ")
        time.sleep(0.2)
        print("     O      ")
        time.sleep(0.2)
        print("     |      ")
        print("tebrikler oyunu kazandınız doğru tahmin")
        break

        tahmin=input("tahmin giriniz: ")
    if tahmin!=kelimeler:
        print("yanlış tahmin")
        time.sleep(0.2)
        print("  --------  ")
        print("     O      ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        hak -= 1
        tahmin = input("tahmin giriniz: ")
    else:
        print("  --------  ")
        time.sleep(0.2)
        print("     O      ")
        time.sleep(0.2)
        print("     |      ")
        print("tebrikler oyunu kazandınız doğru tahmin")
        break

        tahmin=input("tahmin giriniz: ")
    if tahmin!=kelimeler:
        print("yanlış tahmin")
        time.sleep(0.2)
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O /    ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        hak -= 1
        tahmin = input("tahmin giriniz: ")
    else:
        print("  --------  ")
        print("     O      ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        print("tebrikler oyunu kazandınız doğru tahmin")
        break

        tahmin=input("tahmin giriniz: ")
    if tahmin!=kelimeler:
        print("yanlış tahmin:")
        time.sleep(0.2)
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O /|   ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        hak-=1
        tahmin=input("tahmin giriniz: ")
    else:
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O /    ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        print("tebrikler oyunu kazandınız doğru tahmin")
        break

        tahmin = input("tahmin giriniz: ")
    if tahmin != kelimeler:
        print("yanlış tahmin:")
        print("Son hakkınız dikkat edin")
        time.sleep(0.2)
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O_|/   ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        hak -=1
        tahmin=input("tahmin giriniz: ")
    else:
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O /|   ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        print("tebrikler oyunu kazandınız doğru tahmin")
        break

        tahmin=input("tahmin giriniz: ")
    if tahmin!=kelimeler:
        print("yanlış tahmin.. Oyunu kaybettiniz")
        print("     O_|    ")
        time.sleep(0.2)
        print("    /|\      ")
        time.sleep(0.2)
        print("    / \     ")
        break
    else:
        print("  --------  ")
        time.sleep(0.2)
        print("   \ O_|/   ")
        time.sleep(0.2)
        print("     |      ")
        time.sleep(0.2)
        print("    / \     ")
        print("tebrikler oyunu kazandınız doğru cevap")
        break