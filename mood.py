import streamlit as st
import webbrowser

# Dictionary of moods and playlist links
mood_playlist_links = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl",
    "relaxed": "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO",
    "romantic": "https://open.spotify.com/playlist/37i9dQZF1DWVpjAJGB70vU",
    "motivated": "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP",
    "nostalgic": "https://open.spotify.com/playlist/37i9dQZF1DX0SM0LYsmbMT",
    "lonely": "https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn",
    "celebrating": "https://open.spotify.com/playlist/37i9dQZF1DXc6IFF23C9jj",
    "tired": "https://open.spotify.com/playlist/37i9dQZF1DWZd79rJ6a7lp",
    "hopeful": "https://open.spotify.com/playlist/37i9dQZF1DXcZDD7cfEKhW",
    "focused": "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO"
}

# Web App Title
st.set_page_config(page_title="Mood Music Recommender", page_icon="🎧")
st.title("🎧 Mood-Based Music Recommender")
st.markdown("Pick a mood and get a playlist instantly. No webcam, no drama, just vibes.")

# Dropdown for mood selection
mood = st.selectbox("How are you feeling today?", list(mood_playlist_links.keys()))

# Button to play playlist
if st.button("Play on Spotify 🎶"):
    playlist_url = mood_playlist_links.get(mood)
    if playlist_url:
        st.success(f"Enjoy your {mood} playlist! Opening in browser...")
        webbrowser.open(playlist_url)
    else:
        st.error("Oops! That mood's playlist is missing.")
