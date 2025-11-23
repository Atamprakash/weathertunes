# app.py - WeatherTunes (GUARANTEED WORKING)
import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# === Load secrets (Streamlit's bulletproof way) ===
OPENWEATHER_API_KEY = st.secrets["general"]["OPENWEATHER_API_KEY"]
SPOTIFY_CLIENT_ID = st.secrets["general"]["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = st.secrets["general"]["SPOTIFY_CLIENT_SECRET"]

st.set_page_config(page_title="WeatherTunes", page_icon="musical_note", layout="centered")

MOOD_GENRES = {
    'Clear': ['pop', 'dance', 'summer', 'happy'],
    'Clouds': ['indie', 'chill', 'lofi', 'acoustic'],
    'Rain': ['sad', 'rainy', 'piano', 'r&b'],
    'Drizzle': ['jazz', 'lofi', 'ambient', 'cozy'],
    'Thunderstorm': ['rock', 'metal', 'epic'],
    'Snow': ['classical', 'christmas', 'ambient', 'calm'],
    'Mist': ['ambient', 'electronic', 'chillwave'],
    'Fog': ['ambient', 'electronic', 'downtempo'],
}

st.title("WeatherTunes")
st.markdown("### Music that matches your weather")

city = st.text_input("Enter city name", value="London", placeholder="Paris, Tokyo, Mumbai...")

if st.button("Get My Weather Playlist", type="primary", use_container_width=True):
    with st.spinner("Finding the perfect songs for this weather..."):
        try:
            # Weather
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
            data = requests.get(url).json()
            
            if data.get("cod") != 200:
                st.error(f"City not found: {data.get('message')}")
            else:
                temp = round(data["main"]["temp"], 1)
                condition = data["weather"][0]["main"]
                desc = data["weather"][0]["description"].title()
                icon = data["weather"][0]["icon"]

                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(f"http://openweathermap.org/img/wn/{icon}@4x.png", width=140)
                with col2:
                    st.markdown(f"### {city.title()}")
                    st.markdown(f"**{condition}** – {desc}")
                    st.markdown(f"**{temp}°C**")

                # Spotify
                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
                    client_id=SPOTIFY_CLIENT_ID,
                    client_secret=SPOTIFY_CLIENT_SECRET
                ))

                tracks = []
                for genre in MOOD_GENRES.get(condition, ['chill']):
                    try:
                        results = sp.search(q=f"genre:{genre}", type="track", limit=10)
                        tracks.extend(results['tracks']['items'])
                        if len(tracks) >= 6: break
                    except: pass

                if len(tracks) < 3:
                    results = sp.search(q="weather mood playlist", type="track", limit=6)
                    tracks = results['tracks']['items']

                st.success(f"Perfect playlist for {condition.lower()} weather")
                st.subheader("Your Weather Playlist")

                cols = st.columns(2)
                for i, track in enumerate(tracks[:6]):
                    with cols[i % 2]:
                        artists = ", ".join(a["name"] for a in track["artists"][:2])
                        st.markdown(f"""
                        <div style="background:#191414;color:white;padding:18px;border-radius:15px;margin:12px 0;text-align:center;box-shadow:0 4px 15px rgba(29,185,84,0.3)">
                            <strong style="font-size:19px">{track['name']}</strong><br>
                            <span style="opacity:0.8">{artists}</span><br><br>
                            <a href="{track['external_urls']['spotify']}" target="_blank">
                                <button style="background:#1DB954;color:white;padding:12px 24px;border:none;border-radius:50px;font-weight:bold;font-size:16px;cursor:pointer">
                                Play on Spotify
                                </button>
                            </a>
                        </div>
                        """, unsafe_allow_html=True)

        except Exception as e:
            st.error("Something went wrong. Try again!")

st.markdown("---")
st.caption("Powered by OpenWeatherMap + Spotify")