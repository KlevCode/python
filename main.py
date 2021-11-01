import tkinter as tk
from PIL import Image, ImageTk
import Timer



root = tk.Tk()

root.title("Pomodoro-Timer")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Einfügen des Logos
logo = Image.open('/home/hauke/Dokumente/Code/Python/tkinter/large.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Anweisung, Button zu drücken
instructions = tk.Label(root, text="Button klicken um 25-Minuten-Timer zu starten", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# Timer-Klasse

class Timer(time):
  def __init__(self):


# Funktion zum starten des Timers



