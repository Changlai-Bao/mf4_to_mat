# MF4 zu MAT Konverter

Konvertiert MF4-Dateien in MATLAB MAT-Dateien mit `asammdf`.

## Installation

```bash
uv sync
```

## Verwendung

1. MF4-Dateien in `Messdaten_mf4` platzieren
2. Skript ausführen:

```bash
uv run mf4_to_mat.py
```

Konvertierte Dateien werden in `Messdaten_mat` gespeichert.

## Projektstruktur

```
mf4_to_mat/
├── Messdaten_mf4/
├── Messdaten_mat/
├── mf4_to_mat.py
├── pyproject.toml
└── README.md
```
