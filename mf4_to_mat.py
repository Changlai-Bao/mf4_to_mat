import os
from pathlib import Path
from asammdf import MDF

def convert_mf4_to_mat():
    # Relative Pfade zu den Ordnern definieren (basierend auf der Projektstruktur)
    input_dir = Path("Messdaten_mf4/20.03.2026")
    output_dir = Path("Messdaten_mat/20.03.2026")

    # Überprüfen, ob der Eingangsordner existiert
    if not input_dir.exists():
        print(f"Fehler: Der Ordner '{input_dir}' wurde nicht gefunden.")
        return

    # Ausgabeverzeichnis erstellen, falls es noch nicht existiert
    output_dir.mkdir(parents=True, exist_ok=True)

    # Alle .mf4 Dateien im Eingangsordner durchlaufen
    mf4_files = list(input_dir.glob("*.mf4"))
    
    if not mf4_files:
        print(f"Keine .mf4 Dateien im Ordner '{input_dir}' gefunden.")
        return

    print(f"{len(mf4_files)} Dateien gefunden. Starte Konvertierung...")

    for mf4_file in mf4_files:
        print(f"Konvertiere: {mf4_file.name} ...")

        try:
            # MDF-Datei in den Arbeitsspeicher laden
            mdf = MDF(mf4_file)

            # Pfad für die Ausgabedatei definieren 
            # (ohne .mat Endung, da asammdf diese automatisch hinzufügt)
            mat_output_path = output_dir / mf4_file.stem

            # Direkter Export der Daten in das MATLAB (.mat) Format
            # 'format="mat"' nutzt scipy.io.savemat im Hintergrund
            mdf.export(fmt="mat", filename=str(mat_output_path))

            # MDF-Objekt schließen, um Arbeitsspeicher freizugeben
            mdf.close()

            print(f" -> Erfolgreich gespeichert als: {mf4_file.stem}.mat")

        except Exception as e:
            # Fehlerbehandlung, falls eine Datei beschädigt ist
            print(f" -> Fehler bei der Verarbeitung von {mf4_file.name}: {e}")

    print("Alle Konvertierungen abgeschlossen.")

if __name__ == "__main__":
    convert_mf4_to_mat()