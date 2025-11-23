# WeatherTunes

A Python app that recommends music based on real-time weather. Fetches data from OpenWeatherMap, maps to moods, and suggests Spotify songs.

## Requirements
- Python 3.8+
- API Keys: OpenWeatherMap and Spotify (free tiers available)

## Setup
1. Clone or create the project directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Rename `.env.example` to `.env` and add your API keys.

## Running Locally
1. Open a terminal in the `weathertunes` directory.
2. Run: `python main.py`
3. Enter a city name when prompted.
4. View weather, mood, and song recommendations in the console.

## Future Upgrades
- Auto-location: Use geolocation APIs (e.g., ipinfo.io).
- Web deployment: Use Flask/Django for a web interface.
- ML-enhanced: Integrate machine learning for better mood-song mapping (e.g., via scikit-learn).

## Troubleshooting
- Ensure API keys are valid and .env is loaded.
- If Spotify auth fails, check Client ID/Secret.
- Handle rate limits: Free APIs have limits; add error handling as needed.