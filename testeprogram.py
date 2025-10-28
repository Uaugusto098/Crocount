import tkinter as tk
from time import strftime

def atualizar():
    hora = strftime('%H:%M:%S')
    label.config(text=hora)
    label.after(1000, atualizar)  # atualiza a cada 1 segundo

root = tk.Tk()
root.title("Relógio")

label = tk.Label(root, font=('Arial', 48), background='black', foreground='lime')
label.pack(padx=20, pady=20)

atualizar()  # inicia atualização
root.mainloop()
