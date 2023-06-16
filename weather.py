import requests
import json

def hava_durumu_cek(sehir):
    # Hava durumu API'sine istek göndermek için API anahtarınızı buraya girin
    api_anahtari = "API_ANAHTARI"

    # Hava durumu API'si ile istek yapılacak URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}"

    try:
        # Hava durumu verilerini getir
        response = requests.get(url)
        veri = response.json()

        # Verileri işle
        sicaklik = veri["main"]["temp"]
        nem_orani = veri["main"]["humidity"]
        ruzgar_hizi = veri["wind"]["speed"]
        aciklama = veri["weather"][0]["description"]

        # Verileri yazdır
        print(f"{sehir} Hava Durumu:")
        print(f"Sıcaklık: {sicaklik} Kelvin")
        print(f"Nem Oranı: {nem_orani}%")
        print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")
        print(f"Açıklama: {aciklama}")

    except:
        print("Hava durumu bilgisi alınamadı.")

# Kullanıcıdan şehir bilgisini al
sehir = input("Hava durumu bilgisini almak istediğiniz şehri girin: ")

# Hava durumu bilgisini çek ve yazdır
hava_durumu_cek(sehir)
