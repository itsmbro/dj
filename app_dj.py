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

# Non usare evento[0], dato che è un dizionario
if evento:
    nome_evento = evento["nome"]
    data_evento = evento["data"]
    ora_evento = evento["ora"]
    luogo_evento = evento["luogo"]
    locandina_evento = evento["locandina"]
else:
    nome_evento = ""
    data_evento = ""
    ora_evento = ""
    luogo_evento = ""
    locandina_evento = ""

with st.form("Modifica Evento"):
    nome = st.text_input("Nome evento", nome_evento)
    data = st.date_input("Data", value=datetime.today())
    ora = st.time_input("Ora")
    luogo = st.text_input("Luogo", luogo_evento)
    locandina = st.text_input("URL Locandina", locandina_evento)
    invia = st.form_submit_button("Aggiorna")

    if invia:
        nuovo_evento = {
            "nome": nome,
            "data": str(data) + " " + str(ora),
            "luogo": luogo,
            "locandina": locandina
        }
        salva_dati("dati/evento.json", nuovo_evento)  # Salva come dizionario
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
