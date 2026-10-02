import tkinter as tk

raiz = tk.Tk()
raiz.title("¡Alerta!")
raiz.geometry("500x300")
raiz.configure(bg="black")

calavera = tk.Label(
    raiz,
    text="💀",
    font=("Arial", 80),
    bg="black",
    fg="white"
)
calavera.pack(pady=20)

etiqueta = tk.Label(
    raiz,
    text="Te he hackeado bro",
    font=("Arial", 24, "bold"),
    bg="black",
    fg="red"
)
etiqueta.pack()

raiz.mainloop()