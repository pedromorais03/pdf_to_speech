import pyttsx3
from pydub import AudioSegment

conteudos = ["Desenvolvimento motor mês a mês", "Epilepsia", "Paralisia Braquial Obstétrica", "Desenvolvimento neuropsicomotor"]

engine = pyttsx3.init()

for c in conteudos:
   print(f"Gerando..:{c}")
   with open(f"{c}.txt", "r", encoding="utf-8") as file:
      text = file.read()

   engine.save_to_file(text, f"{c}.wav")
   engine.runAndWait()
   print("Ok")