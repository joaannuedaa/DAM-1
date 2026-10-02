import tkinter as tk
from tkinter import ttk, messagebox


# ─────────────────────────────────────────────
# COLORES
# ─────────────────────────────────────────────

FONDO = "#0b1120"
PANEL = "#111827"
PANEL2 = "#1e293b"
AZUL = "#38bdf8"
VERDE = "#22c55e"
ROJO = "#f43f5e"
BLANCO = "#f8fafc"
GRIS = "#94a3b8"


# ─────────────────────────────────────────────
# FUNCIONES
# ─────────────────────────────────────────────

def calcular():
    try:
        precio = float(entrada_precio.get().replace(",", "."))

        if precio < 0:
            raise ValueError

        descuento = float(
            entrada_descuento.get().replace(",", ".") or 0
        )

        if descuento < 0 or descuento > 100:
            raise ValueError

        iva_porcentaje = float(combo_iva.get().replace("%", ""))

        # Aplicar descuento
        importe_descuento = precio * descuento / 100
        base = precio - importe_descuento

        # Calcular IVA
        iva = base * iva_porcentaje / 100
        total = base + iva

        # Mostrar resultados
        resultado_base.config(
            text=f"{precio:.2f} €"
        )

        resultado_descuento.config(
            text=f"- {importe_descuento:.2f} €"
        )

        resultado_iva.config(
            text=f"+ {iva:.2f} €"
        )

        resultado_total.config(
            text=f"{total:.2f} €"
        )

        # Guardar historial
        historial.insert(
            0,
            f"{precio:.2f} €  →  {total:.2f} €"
        )

        mensaje.config(
            text="✓ Cálculo realizado correctamente",
            fg=VERDE
        )

    except ValueError:
        mensaje.config(
            text="⚠ Introduce valores válidos",
            fg=ROJO
        )


def limpiar():
    entrada_precio.delete(0, tk.END)
    entrada_descuento.delete(0, tk.END)

    resultado_base.config(text="0.00 €")
    resultado_descuento.config(text="- 0.00 €")
    resultado_iva.config(text="+ 0.00 €")
    resultado_total.config(text="0.00 €")

    mensaje.config(
        text="Introduce los datos para comenzar",
        fg=GRIS
    )


def borrar_historial():
    historial.delete(0, tk.END)


# ─────────────────────────────────────────────
# VENTANA
# ─────────────────────────────────────────────

ventana = tk.Tk()

ventana.title("Calculadora de IVA PRO")
ventana.geometry("720x720")
ventana.configure(bg=FONDO)
ventana.resizable(False, False)


# ─────────────────────────────────────────────
# CABECERA
# ─────────────────────────────────────────────

tk.Label(
    ventana,
    text="💶  IVA PRO",
    font=("Arial", 32, "bold"),
    bg=FONDO,
    fg=AZUL
).pack(pady=(30, 5))

tk.Label(
    ventana,
    text="Calculadora profesional de impuestos",
    font=("Arial", 12),
    bg=FONDO,
    fg=GRIS
).pack(pady=(0, 25))


# ─────────────────────────────────────────────
# PANEL DE ENTRADA
# ─────────────────────────────────────────────

panel = tk.Frame(
    ventana,
    bg=PANEL,
    padx=30,
    pady=25
)

panel.pack(fill="x", padx=45)


tk.Label(
    panel,
    text="PRECIO",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).grid(row=0, column=0, sticky="w")

entrada_precio = tk.Entry(
    panel,
    font=("Arial", 20, "bold"),
    bg=PANEL2,
    fg=BLANCO,
    insertbackground=BLANCO,
    relief="flat",
    justify="right"
)

entrada_precio.grid(
    row=1,
    column=0,
    padx=(0, 15),
    pady=(5, 20),
    ipady=8
)


tk.Label(
    panel,
    text="IVA",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).grid(row=0, column=1, sticky="w")

combo_iva = ttk.Combobox(
    panel,
    values=["4%", "10%", "21%"],
    state="readonly",
    font=("Arial", 14),
    width=10
)

combo_iva.set("21%")

combo_iva.grid(
    row=1,
    column=1,
    padx=(0, 15),
    pady=(5, 20),
    ipady=8
)


tk.Label(
    panel,
    text="DESCUENTO",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).grid(row=0, column=2, sticky="w")

entrada_descuento = tk.Entry(
    panel,
    font=("Arial", 20, "bold"),
    bg=PANEL2,
    fg=BLANCO,
    insertbackground=BLANCO,
    relief="flat",
    justify="right",
    width=8
)

entrada_descuento.grid(
    row=1,
    column=2,
    pady=(5, 20),
    ipady=8
)


# ─────────────────────────────────────────────
# BOTONES
# ─────────────────────────────────────────────

botones = tk.Frame(
    ventana,
    bg=FONDO
)

botones.pack(pady=20)


tk.Button(
    botones,
    text="CALCULAR  🚀",
    command=calcular,
    font=("Arial", 13, "bold"),
    bg=AZUL,
    fg=FONDO,
    activebackground="#0ea5e9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=12
).pack(side="left", padx=8)


tk.Button(
    botones,
    text="LIMPIAR  ✕",
    command=limpiar,
    font=("Arial", 13, "bold"),
    bg=PANEL2,
    fg=BLANCO,
    activebackground="#334155",
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=12
).pack(side="left", padx=8)


# ─────────────────────────────────────────────
# RESULTADOS
# ─────────────────────────────────────────────

resultado = tk.Frame(
    ventana,
    bg=PANEL,
    padx=30,
    pady=20
)

resultado.pack(
    fill="x",
    padx=45
)


def fila(texto, variable, color=BLANCO):
    tk.Label(
        resultado,
        text=texto,
        font=("Arial", 12),
        bg=PANEL,
        fg=GRIS
    ).pack(anchor="w")

    tk.Label(
        resultado,
        textvariable=variable,
        font=("Arial", 16, "bold"),
        bg=PANEL,
        fg=color
    ).pack(anchor="w", pady=(0, 10))


base_var = tk.StringVar(value="0.00 €")
descuento_var = tk.StringVar(value="- 0.00 €")
iva_var = tk.StringVar(value="+ 0.00 €")
total_var = tk.StringVar(value="0.00 €")


resultado_base = tk.Label(
    resultado,
    text="0.00 €",
    font=("Arial", 16, "bold"),
    bg=PANEL,
    fg=BLANCO
)

resultado_base.pack(anchor="e")


tk.Label(
    resultado,
    text="BASE IMPONIBLE",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).place(x=30, y=25)


resultado_descuento = tk.Label(
    resultado,
    text="- 0.00 €",
    font=("Arial", 16, "bold"),
    bg=PANEL,
    fg=ROJO
)

resultado_descuento.pack(anchor="e")


tk.Label(
    resultado,
    text="DESCUENTO",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).place(x=30, y=70)


resultado_iva = tk.Label(
    resultado,
    text="+ 0.00 €",
    font=("Arial", 16, "bold"),
    bg=PANEL,
    fg=AZUL
)

resultado_iva.pack(anchor="e")


tk.Label(
    resultado,
    text="IVA",
    font=("Arial", 10, "bold"),
    bg=PANEL,
    fg=GRIS
).place(x=30, y=115)


resultado_total = tk.Label(
    resultado,
    text="0.00 €",
    font=("Arial", 26, "bold"),
    bg=PANEL,
    fg=VERDE
)

resultado_total.pack(anchor="e", pady=(5, 0))


tk.Label(
    resultado,
    text="TOTAL",
    font=("Arial", 12, "bold"),
    bg=PANEL,
    fg=GRIS
).place(x=30, y=160)


# ─────────────────────────────────────────────
# MENSAJE
# ─────────────────────────────────────────────

mensaje = tk.Label(
    ventana,
    text="Introduce los datos para comenzar",
    font=("Arial", 10),
    bg=FONDO,
    fg=GRIS
)

mensaje.pack(pady=12)


# ─────────────────────────────────────────────
# HISTORIAL
# ─────────────────────────────────────────────

tk.Label(
    ventana,
    text="ÚLTIMOS CÁLCULOS",
    font=("Arial", 10, "bold"),
    bg=FONDO,
    fg=GRIS
).pack()


historial = tk.Listbox(
    ventana,
    height=4,
    width=55,
    bg=PANEL2,
    fg=BLANCO,
    font=("Arial", 11),
    relief="flat",
    highlightthickness=0
)

historial.pack(pady=8)


tk.Button(
    ventana,
    text="Borrar historial",
    command=borrar_historial,
    font=("Arial", 9),
    bg=FONDO,
    fg=GRIS,
    relief="flat",
    cursor="hand2"
).pack()


# ─────────────────────────────────────────────
# ENTER = CALCULAR
# ─────────────────────────────────────────────

ventana.bind(
    "<Return>",
    lambda event: calcular()
)


entrada_precio.focus()


# ─────────────────────────────────────────────
# ARRANCAR
# ─────────────────────────────────────────────

ventana.mainloop()