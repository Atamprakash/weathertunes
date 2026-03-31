# 🌦️ WeatherTunes

A Python app that recommends music based on real-time weather. Fetches data from OpenWeatherMap, maps to moods, and suggests Spotify songs.

## Requirements
- Python 3.8+
- API Keys: OpenWeatherMap and Spotify (free tiers available)

## 🖼️ Project Gallery
![App Screenshot 1](images/screenshot1.png)
![App Screenshot 2](images/screenshot2.png)
![App Screenshot 3](images/screenshot3.png)

## 🚀 Key Features
- **Real-Time Weather:** Fetches live data via OpenWeatherMap API.
- **Mood Mapping:** Translates conditions (Rain, Sun, etc.) into musical genres.
- **Spotify Integration:** Displays playable tracks directly in the UI.

## ⚠️ Technical Note (Spotify API)
The Weather integration is fully functional. However, due to current Spotify Developer policies, the **Spotify Recommendation** feature requires a **Spotify Premium** account for successful authentication and data retrieval in the live environment.

## 🛠️ How to Run
1. **Clone Repo:** `git clone https://github.com/your-username/WeatherTunes.git`
2. **Install:** `pip install -r requirements.txt`
3. **API Keys:** Add keys to your Streamlit Secrets dashboard or `.streamlit/secrets.toml`.
4. **Launch:** `streamlit run app.py`

## Future Upgrades
- Auto-location: Use geolocation APIs (e.g., ipinfo.io).
- Web deployment: Use Flask/Django for a web interface.
- ML-enhanced: Integrate machine learning for better mood-song mapping (e.g., via scikit-learn).

## ⚖️ License
Licensed under the **MIT License**.
