import streamlit as st
from utils import carica_dati, salva_dati
from datetime import datetime

st.set_page_config(page_title="DJ Request", layout="centered")

menu = st.sidebar.selectbox("Menu", ["Richiedi canzone", "Prossimo evento", "Playlist", "Contatti DJ"])

if menu == "Richiedi canzone":
    st.header("🎶 Richiedi una canzone")
    canzone = st.text_input("Nome canzone")
    dedica = st.text_input("Dedica (opzionale)")
    if st.button("Invia richiesta"):
        if canzone:
            nuove_richieste = carica_dati("dati/richieste.json")
            nuove_richieste.append({"canzone": canzone, "dedica": dedica})
            salva_dati("dati/richieste.json", nuove_richieste)
            st.success("Richiesta inviata!")
        else:
            st.warning("Inserisci almeno il nome della canzone.")

elif menu == "Prossimo evento":
    st.header("📅 Prossimo evento")
    evento = carica_dati("dati/evento.json")
    if evento:
        evento = evento[0]
        st.subheader(evento["nome"])
        st.write(f"📍 {evento['luogo']}")
        st.write(f"🕒 {evento['data']}")
        if evento["locandina"]:
            st.image(evento["locandina"])
        # Timer countdown (semplificato)
        evento_datetime = datetime.strptime(evento["data"], "%Y-%m-%d %H:%M:%S")
        tempo_mancante = evento_datetime - datetime.now()
        st.info(f"⏳ Mancano: {tempo_mancante}")

elif menu == "Playlist":
    st.header("🎵 Playlist Predefinita")
    playlist = carica_dati("dati/playlist.json")
    for c in playlist:
        st.write(f"- {c}")

elif menu == "Contatti DJ":
    st.header("📧 Contatti DJ")
    st.write("Per info o richieste: **dj@email.com**")
