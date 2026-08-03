import os
import sys

# Das Paket wird durch das Setup oben direkt im System registriert
try:
    from core.cloner import KokoClone
except ImportError:
    # Fallback, falls die interne Struktur des Ziel-Repos direkt über core importiert werden muss
    sys.path.append(os.path.abspath("kokoclone_src"))
    from core.cloner import KokoClone

def generate_voice_clone():
    ref_audio = "reference.wav"
    output_audio = "output.wav"
    text_payload = os.environ.get("INPUT_TEXT", "Fallback Text")

    if not os.path.exists(ref_audio):
        raise FileNotFoundError(f"Bitte lade die Datei '{ref_audio}' in dein Hauptverzeichnis hoch.")

    print("KokoClone Engine wird gestartet...")
    cloner = KokoClone()

    print(f"Generiere Audio für: '{text_payload}'")
    cloner.generate(
        text=text_payload,
        lang="en",
        reference_audio=ref_audio,
        output_path=output_audio,
    )
    print("Audio erfolgreich generiert!")

if __name__ == "__main__":
    generate_voice_clone()
