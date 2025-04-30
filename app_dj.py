import streamlit as st
from utils import carica_dati, salva_dati
from datetime import datetime

st.set_page_config(page_title="Area DJ", layout="wide")

st.title("🎧 Area DJ")

# Mostra richieste
st.subheader("🎶 Richieste ricevute")
richieste = carica_dati("dati/richieste.json")
for r in richieste:
    st.write(f"**{r['canzone']}** dedicata a *{r['dedica']}*")

# Modifica evento
st.subheader("📅 Prossimo evento")
evento = carica_dati("dati/evento.json")
if evento:
    evento = evento[0]
else:
    evento = {"nome": "", "data": "", "luogo": "", "locandina": ""}

with st.form("Modifica Evento"):
    nome = st.text_input("Nome evento", evento["nome"])
    data = st.date_input("Data", value=datetime.today())
    ora = st.time_input("Ora")
    luogo = st.text_input("Luogo", evento["luogo"])
    locandina = st.text_input("URL Locandina", evento["locandina"])
    invia = st.form_submit_button("Aggiorna")

    if invia:
        nuovo_evento = {
            "nome": nome,
            "data": str(data) + " " + str(ora),
            "luogo": luogo,
            "locandina": locandina
        }
        salva_dati("dati/evento.json", [nuovo_evento])
        st.success("Evento aggiornato!")

# Playlist
st.subheader("🎵 Playlist")
playlist = carica_dati("dati/playlist.json")
nuova = st.text_input("Aggiungi canzone alla playlist")
if st.button("Aggiungi"):
    playlist.append(nuova)
    salva_dati("dati/playlist.json", playlist)
    st.success("Aggiunta!")

for c in playlist:
    st.write(f"- {c}")
