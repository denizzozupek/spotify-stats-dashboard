# Spotify Stats Dashboard

Bu proje, Spotify hesabınızla giriş yaparak dinleme geçmişinizi, en çok dinlediğiniz şarkıları ve sanatçıları görüntüleyebileceğiniz bir Flask web uygulamasıdır.

## Özellikler

- **Spotify ile Giriş Yapma**: OAuth 2.0 kullanarak güvenli giriş.
- **Kullanıcı Profili**: Profil bilgilerinizi görüntüleyin.
- **Son Çalınanlar**: Son dinlediğiniz şarkıların listesi.
- **En Çok Dinlenenler**: Belirli zaman aralıklarında (kısa, orta, uzun dönem) en çok dinlediğiniz şarkılar ve sanatçılar.

## Gereksinimler

Bu projeyi çalıştırmak için bilgisayarınızda Python kurulu olmalıdır. Ayrıca aşağıdaki kütüphanelere ihtiyacınız vardır:

- Flask
- requests
- python-dotenv

## Kurulum

1. **Projeyi Klonlayın:**

   ```bash
   git clone https://github.com/kullaniciadi/spotify-stats-dashboard.git
   cd spotify-stats-dashboard
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**

   ```bash
   pip install flask requests python-dotenv
   ```

3. **Spotify Uygulaması Oluşturun:**

   - [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) adresine gidin.
   - Yeni bir uygulama oluşturun ("Create App").
   - "Edit Settings" kısmına gidin ve **Redirect URI** olarak şunu ekleyin:
     `http://127.0.0.1:8081/callback/q`
   - **Client ID** ve **Client Secret** değerlerini not edin.

4. **Çevresel Değişkenleri Ayarlayın:**

   Proje ana dizininde `.env` adında bir dosya oluşturun (veya `api/.env` yolunu kontrol edin, proje yapısına göre ana dizinde olması önerilir ancak kod `api/spotify_requests.py` içinde `load_dotenv()` çağırıyor, bu yüzden `.env` dosyasını `app.py`'nin olduğu ana dizine koymanız ve `api/spotify_requests.py`'nin bunu okuyabildiğinden emin olmanız gerekir. Kodun mevcut yapısında `api` klasörü içindeki `spotify_requests.py` `load_dotenv()` çağırıyor, bu genellikle çalıştırılan dizindeki .env dosyasını arar).

   `.env` dosyasına aşağıdaki bilgileri ekleyin:

   ```env
   CLIENT_ID=sizin_spotify_client_id_degeriniz
   CLIENT_SECRET=sizin_spotify_client_secret_degeriniz
   FLASK_SECRET_KEY=rastgele_guvenli_bir_anahtar
   ```

## Çalıştırma

Uygulamayı başlatmak için terminalde şu komutu çalıştırın:

```bash
python app.py
```

Tarayıcınızda `http://127.0.0.1:8081` adresine gidin.

## Proje Yapısı

- `app.py`: Ana Flask uygulaması ve rotalar.
- `api/`: Spotify API isteklerini yöneten modüller.
- `templates/`: HTML şablonları.
- `static/`: CSS ve statik dosyalar.

## Lisans

Bu proje açık kaynaklıdır ve geliştirmeye açıktır.
