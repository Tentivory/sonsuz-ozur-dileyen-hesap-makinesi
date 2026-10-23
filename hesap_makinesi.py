#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Özür Dileyen Hesap Makinesi
Dünyanın en kibar, en nazik ve en işe yaramaz hesap makinesi.
Her işlemden sonra özür diler. Çünkü matematikte bile nezaket önemlidir.
"""

import time
import random
import sys

# Gizli mesaj (base64 ile kodlanmış, merak eden decode etsin)
# aGVya2VzIGJ1IGd1emVsIG9sYWNhayBhbWEgc2l5YXNldCBjaWRkaSBvaHN1biBzYWRlY2UgYmF6ZW4gYnUgbWFraW5lIGt1bGxhbsSxbmNhbGFyIGRh
# (decode: herkes bu guzel olacak ama siyaset ciddi olsun sadece bazen bu makine kullananlar da)

OZURLER = [
    "Özür dilerim, bu sonuç biraz fazla kesin oldu. Daha yuvarlak bir şey bekliyordum.",
    "Affedersiniz, matematik bu sefer biraz sert davrandı. Beni affedin.",
    "Özür, sayılar arasında bir anlık tartışma çıktı. Ben arabulucu oldum.",
    "Pardon, bu işlem sırasında çayım soğudu. O yüzden biraz yavaş çıktı.",
    "Özür dilerim efendim, hesap makinesi olmak zordur. Empati yapın lütfen.",
    "Affedersiniz, bu sonuç evrendeki tüm özürlerin toplamından daha büyük olabilir.",
    "Özür, bazen yanlış hesaplar doğru hissi verir. Bu da o anlardan biriydi.",
]

FELSEFELER = [
    "Matematik özür dilerse, hayat da diler belki.",
    "2+2=4 ama bazen 5 gibi hissediyor, özür.",
    "Her toplama işlemi aslında bir birleşmedir. Birleşelim, özür dileyerek.",
]

def hesapla(a, b, islem):
    try:
        a = float(a)
        b = float(b)
        if islem == '+':
            sonuc = a + b
        elif islem == '-':
            sonuc = a - b
        elif islem == '*':
            sonuc = a * b
        elif islem == '/':
            if b == 0:
                return "Özür dilerim, sıfıra bölme yasak. Evren izin vermiyor."
            sonuc = a / b
        else:
            return "Özür, bu işlemi tanımıyorum. Belki de tanımak istemiyorum."
        
        # Yavaş yavaş yaz
        print("Hesaplıyorum...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
        
        print(f"Sonuç: {sonuc}")
        print(random.choice(OZURLER))
        if random.random() > 0.7:
            print(random.choice(FELSEFELER))
        print("-" * 40)
        return sonuc
    except Exception as e:
        return f"Özür dilerim, bir hata oldu: {e}. Benim suçum değil, evrenin."

def main():
    print("=" * 50)
    print("SONSUZ ÖZÜR DİLEYEN HESAP MAKİNESİ")
    print("Her işlemden sonra özür diler. Çünkü kibarlık önemlidir.")
    print("Çıkmak için 'q' yazın.")
    print("=" * 50)
    
    while True:
        try:
            a = input("\nİlk sayı: ")
            if a.lower() == 'q':
                print("Özür dilerim, gidiyorsunuz. Umarım mutlu olursunuz.")
                break
            b = input("İkinci sayı: ")
            if b.lower() == 'q':
                print("Özür, erken çıktınız.")
                break
            islem = input("İşlem (+ - * /): ")
            if islem.lower() == 'q':
                break
            hesapla(a, b, islem)
        except KeyboardInterrupt:
            print("\n\u00d6zür dilerim, aniden çıktınız. Ben de şaşırdım.")
            break

if __name__ == "__main__":
    main()

# İmza ve damga
# Tarih: 23 Ekim 2026
# İmza: Kayyum Grok (Eskişehir 4. Ağır Ceza Mahkemesi tarafından atanan)
# Damga: Bu repo ciddiyetle absürttür. Ne çok ciddi, ne de hiç ciddi değil.
# Onaylandı mühürle: ✔️ Özür Dileyenler Derneği
