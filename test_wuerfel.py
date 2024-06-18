import tkinter as Tk
from random import randint, seed

# Initialisiere den Zufallszahlengenerator
seed()

# Globale Variable für die Anzahl der Würfe
zaehler = 0

def wuerfeln():
    global zaehler
    augenzahl = randint(1, 6)
    zaehler += 1
    result_label.config(text=f"Wurf {zaehler}: {augenzahl}")

    if augenzahl == 6:
        count_label.config(text=f"Anzahl der Versuche: {zaehler}")

# Erstelle das Hauptfenster
root = Tk.Tk()
root.title("Würfel-Simulator")

# Erstelle und platziere die Labels und den Button
start_button = Tk.Button(root, text="Würfeln", command=wuerfeln)
start_button.pack(pady=20)

result_label = Tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

count_label = Tk.Label(root, text="", font=("Helvetica", 16))
count_label.pack(pady=10)

# Starte die GUI-Schleife
root.mainloop()
