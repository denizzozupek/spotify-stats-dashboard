# Spotify Stats Dashboard

<<<<<<< HEAD
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
=======
This project is a Flask web application that allows you to log in with your Spotify account to view your listening history, top tracks, and top artists.

## Features

  - **Log in with Spotify**: Secure login using OAuth 2.0.
  - **User Profile**: View your profile information.
  - **Recently Played**: A list of your recently played tracks.
  - **Top Items**: Your most listened-to songs and artists over specific time ranges (short, medium, and long term).


## Screenshots

<img width="1895" height="907" alt="image" src="https://github.com/user-attachments/assets/6a755968-4449-49f7-bf71-76f35af84636" />


## Requirements

To run this project, you must have Python installed on your computer. Additionally, you need the following libraries:

  - Flask
  - requests
  - python-dotenv

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/username/spotify-stats-dashboard.git
    cd spotify-stats-dashboard
    ```

2.  **Install Required Libraries:**

    ```bash
    pip install flask requests python-dotenv
    ```

3.  **Create a Spotify App:**

      - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
      - Create a new application ("Create App").
      - Go to "Edit Settings" and add the following as the **Redirect URI**:
        `http://127.0.0.1:8081/callback/q`
      - Note down the **Client ID** and **Client Secret** values.

4.  **Set Up Environment Variables:**

    Create a file named `.env` in the root directory of the project.

    *(Note: Depending on your project structure, ensure the `.env` file is placed where `api/spotify_requests.py` can access it. Since the code calls `load_dotenv()`, placing it in the main directory where `app.py` runs is usually the correct approach.)*

    Add the following information to the `.env` file:

    ```env
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    FLASK_SECRET_KEY=a_random_secure_key
    ```

## Usage

To start the application, run the following command in your terminal:
>>>>>>> d54fdb90db0fcc02764857c1cb3179e390e67908

```bash
python app.py
```

<<<<<<< HEAD
Tarayıcınızda `http://127.0.0.1:8081` adresine gidin.

## Proje Yapısı

- `app.py`: Ana Flask uygulaması ve rotalar.
- `api/`: Spotify API isteklerini yöneten modüller.
- `templates/`: HTML şablonları.
- `static/`: CSS ve statik dosyalar.

## Lisans

Bu proje açık kaynaklıdır ve geliştirmeye açıktır.
=======
Open your web browser and navigate to `http://127.0.0.1:8081`.

## Project Structure

  - `app.py`: Main Flask application and routes.
  - `api/`: Modules handling Spotify API requests.
  - `templates/`: HTML templates.
  - `static/`: CSS and static files.

## License

This project is open source and open for development.

-----

**Bir sonraki adım:**
Projeni GitHub'a yüklerken gereksiz dosyaların (örneğin `.env` veya `__pycache__` klasörlerinin) yüklenmemesi çok önemlidir. Bunun için bir **`.gitignore`** dosyası oluşturmanı ister misin?
>>>>>>> d54fdb90db0fcc02764857c1cb3179e390e67908
