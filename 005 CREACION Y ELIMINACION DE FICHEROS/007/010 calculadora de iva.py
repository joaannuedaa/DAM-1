import tkinter as tk

def calcular_iva():
    basenumero = base.get()
    basenumero = float(basenumero)
    iva = basenumero * 0.21
    resultado.config(text=iva)

ventana = tk.Tk()

base = tk.Entry(ventana)
base.pack(padx=20,pady=20)

boton_calcular = tk.Button(ventana, text="Calcular IVA", command=calcular_iva)
boton_calcular.pack(padx=20,pady=20)

resultado = tk.Label(ventana, text="resultado")
resultado.pack(padx=20,pady=20)

ventana.mainloop()