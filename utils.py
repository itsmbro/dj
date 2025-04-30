import json
from pathlib import Path

def carica_dati(percorso):
    if not Path(percorso).exists():
        return []
    with open(percorso, 'r', encoding='utf-8') as f:
        return json.load(f)

def salva_dati(percorso, dati):
    with open(percorso, 'w', encoding='utf-8') as f:
        json.dump(dati, f, indent=2, ensure_ascii=False)
