# Spotify Stats Dashboard

This project is a Flask web application that allows you to log in with your Spotify account to view your listening history, top tracks, and top artists.

## Features

  - **Log in with Spotify**: Secure login using OAuth 2.0.
  - **User Profile**: View your profile information.
  - **Recently Played**: A list of your recently played tracks.
  - **Top Items**: Your most listened-to songs and artists over specific time ranges (short, medium, and long term).

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

```bash
python app.py
```

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
