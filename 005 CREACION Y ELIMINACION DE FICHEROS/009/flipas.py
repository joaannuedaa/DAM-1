import tkinter as tk
from tkinter import messagebox
import re
import time


# ============================================================
# CONFIGURACIÓN
# ============================================================

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

BG_COLOR = "#0b1020"
CARD_COLOR = "#151c32"
INPUT_COLOR = "#202944"
TEXT_COLOR = "#ffffff"
SECONDARY_TEXT = "#8e9ab8"
ACCENT = "#6c63ff"
ACCENT_HOVER = "#8179ff"
ERROR_COLOR = "#ff5c7a"
SUCCESS_COLOR = "#42d392"


# ============================================================
# APLICACIÓN PRINCIPAL
# ============================================================

class LoginApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Nova — Iniciar sesión")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(900, 600)
        self.configure(bg=BG_COLOR)

        self.password_visible = False
        self.email_focused = False
        self.password_focused = False

        self.create_background()
        self.create_login_card()

        # Centrar inicialmente
        self.after(100, self.center_window)

    # --------------------------------------------------------
    # CENTRAR VENTANA
    # --------------------------------------------------------

    def center_window(self):
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    # --------------------------------------------------------
    # FONDO
    # --------------------------------------------------------

    def create_background(self):

        self.canvas = tk.Canvas(
            self,
            bg=BG_COLOR,
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind(
            "<Configure>",
            self.draw_background
        )

    def draw_background(self, event=None):

        self.canvas.delete("background")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Fondo por capas para dar sensación de degradado
        colors = [
            "#0b1020",
            "#0d1225",
            "#10162b",
            "#12182f",
            "#151b33"
        ]

        section_height = max(height // len(colors), 1)

        for i, color in enumerate(colors):
            self.canvas.create_rectangle(
                0,
                i * section_height,
                width,
                (i + 1) * section_height + 5,
                fill=color,
                outline="",
                tags="background"
            )

        # Círculos decorativos
        self.canvas.create_oval(
            -180,
            -180,
            260,
            260,
            fill="#171d48",
            outline="",
            tags="background"
        )

        self.canvas.create_oval(
            width - 300,
            height - 300,
            width + 100,
            height + 100,
            fill="#171d48",
            outline="",
            tags="background"
        )

        # Brillo central
        self.canvas.create_oval(
            width // 2 - 350,
            height // 2 - 350,
            width // 2 + 350,
            height // 2 + 350,
            outline="#171d3c",
            width=2,
            tags="background"
        )

    # --------------------------------------------------------
    # TARJETA DE LOGIN
    # --------------------------------------------------------

    def create_login_card(self):

        self.card = tk.Frame(
            self.canvas,
            bg=CARD_COLOR,
            width=430,
            height=570
        )

        self.card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Borde visual
        self.card_border = tk.Frame(
            self.canvas,
            bg="#293252",
            width=438,
            height=578
        )

        self.card_border.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.card.lift()

        self.build_card()

    # --------------------------------------------------------
    # CONTENIDO DE LA TARJETA
    # --------------------------------------------------------

    def build_card(self):

        # Logo
        logo = tk.Label(
            self.card,
            text="✦",
            font=("Arial", 32, "bold"),
            bg=CARD_COLOR,
            fg=ACCENT
        )

        logo.pack(pady=(35, 5))

        # Título
        title = tk.Label(
            self.card,
            text="Bienvenido de nuevo",
            font=("Arial", 24, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        )

        title.pack()

        # Subtítulo
        subtitle = tk.Label(
            self.card,
            text="Inicia sesión para continuar",
            font=("Arial", 10),
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT
        )

        subtitle.pack(pady=(7, 28))

        # ----------------------------------------------------
        # EMAIL
        # ----------------------------------------------------

        email_label = tk.Label(
            self.card,
            text="Correo electrónico",
            font=("Arial", 10, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            anchor="w"
        )

        email_label.pack(
            fill="x",
            padx=45
        )

        self.email_frame = tk.Frame(
            self.card,
            bg=INPUT_COLOR,
            height=48
        )

        self.email_frame.pack(
            fill="x",
            padx=45,
            pady=(7, 18)
        )

        self.email_icon = tk.Label(
            self.email_frame,
            text="✉",
            font=("Arial", 14),
            bg=INPUT_COLOR,
            fg=SECONDARY_TEXT
        )

        self.email_icon.pack(
            side="left",
            padx=(14, 5)
        )

        self.email_entry = tk.Entry(
            self.email_frame,
            font=("Arial", 11),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            border=0,
            relief="flat"
        )

        self.email_entry.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.email_entry.bind(
            "<FocusIn>",
            self.email_focus_in
        )

        self.email_entry.bind(
            "<FocusOut>",
            self.email_focus_out
        )

        # ----------------------------------------------------
        # PASSWORD
        # ----------------------------------------------------

        password_label = tk.Label(
            self.card,
            text="Contraseña",
            font=("Arial", 10, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            anchor="w"
        )

        password_label.pack(
            fill="x",
            padx=45
        )

        self.password_frame = tk.Frame(
            self.card,
            bg=INPUT_COLOR,
            height=48
        )

        self.password_frame.pack(
            fill="x",
            padx=45,
            pady=(7, 8)
        )

        self.password_icon = tk.Label(
            self.password_frame,
            text="●",
            font=("Arial", 12),
            bg=INPUT_COLOR,
            fg=SECONDARY_TEXT
        )

        self.password_icon.pack(
            side="left",
            padx=(14, 5)
        )

        self.password_entry = tk.Entry(
            self.password_frame,
            font=("Arial", 11),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            border=0,
            relief="flat",
            show="•"
        )

        self.password_entry.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.password_entry.bind(
            "<FocusIn>",
            self.password_focus_in
        )

        self.password_entry.bind(
            "<FocusOut>",
            self.password_focus_out
        )

        # Botón mostrar contraseña
        self.show_password_button = tk.Button(
            self.password_frame,
            text="◉",
            font=("Arial", 11),
            bg=INPUT_COLOR,
            fg=SECONDARY_TEXT,
            activebackground=INPUT_COLOR,
            activeforeground=TEXT_COLOR,
            border=0,
            cursor="hand2",
            command=self.toggle_password
        )

        self.show_password_button.pack(
            side="right",
            padx=12
        )

        # ----------------------------------------------------
        # OPCIONES
        # ----------------------------------------------------

        options = tk.Frame(
            self.card,
            bg=CARD_COLOR
        )

        options.pack(
            fill="x",
            padx=45,
            pady=(8, 22)
        )

        self.remember_var = tk.BooleanVar()

        remember = tk.Checkbutton(
            options,
            text="Recordarme",
            variable=self.remember_var,
            font=("Arial", 9),
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT,
            activebackground=CARD_COLOR,
            activeforeground=TEXT_COLOR,
            selectcolor=INPUT_COLOR,
            border=0,
            highlightthickness=0
        )

        remember.pack(side="left")

        forgot = tk.Label(
            options,
            text="¿Olvidaste tu contraseña?",
            font=("Arial", 9, "bold"),
            bg=CARD_COLOR,
            fg=ACCENT,
            cursor="hand2"
        )

        forgot.pack(side="right")

        forgot.bind(
            "<Button-1>",
            lambda e: self.forgot_password()
        )

        forgot.bind(
            "<Enter>",
            lambda e: forgot.config(fg=ACCENT_HOVER)
        )

        forgot.bind(
            "<Leave>",
            lambda e: forgot.config(fg=ACCENT)
        )

        # ----------------------------------------------------
        # BOTÓN LOGIN
        # ----------------------------------------------------

        self.login_button = tk.Button(
            self.card,
            text="INICIAR SESIÓN",
            font=("Arial", 11, "bold"),
            bg=ACCENT,
            fg="white",
            activebackground=ACCENT_HOVER,
            activeforeground="white",
            border=0,
            cursor="hand2",
            height=2,
            command=self.login
        )

        self.login_button.pack(
            fill="x",
            padx=45
        )

        self.login_button.bind(
            "<Enter>",
            self.login_hover
        )

        self.login_button.bind(
            "<Leave>",
            self.login_leave
        )

        # ----------------------------------------------------
        # SEPARADOR
        # ----------------------------------------------------

        separator = tk.Frame(
            self.card,
            bg=CARD_COLOR
        )

        separator.pack(
            fill="x",
            padx=45,
            pady=25
        )

        line1 = tk.Frame(
            separator,
            bg="#2a3352",
            height=1
        )

        line1.pack(
            side="left",
            fill="x",
            expand=True,
            pady=7
        )

        or_text = tk.Label(
            separator,
            text="  O  ",
            font=("Arial", 8),
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT
        )

        or_text.pack(side="left")

        line2 = tk.Frame(
            separator,
            bg="#2a3352",
            height=1
        )

        line2.pack(
            side="left",
            fill="x",
            expand=True,
            pady=7
        )

        # ----------------------------------------------------
        # BOTÓN GOOGLE
        # ----------------------------------------------------

        google_button = tk.Button(
            self.card,
            text="G    Continuar con Google",
            font=("Arial", 10, "bold"),
            bg=INPUT_COLOR,
            fg=TEXT_COLOR,
            activebackground="#293452",
            activeforeground=TEXT_COLOR,
            border=0,
            cursor="hand2",
            height=2,
            command=self.google_login
        )

        google_button.pack(
            fill="x",
            padx=45
        )

        # ----------------------------------------------------
        # REGISTRO
        # ----------------------------------------------------

        register_frame = tk.Frame(
            self.card,
            bg=CARD_COLOR
        )

        register_frame.pack(
            pady=(22, 0)
        )

        text = tk.Label(
            register_frame,
            text="¿No tienes una cuenta?",
            font=("Arial", 9),
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT
        )

        text.pack(side="left")

        register = tk.Label(
            register_frame,
            text=" Crear cuenta",
            font=("Arial", 9, "bold"),
            bg=CARD_COLOR,
            fg=ACCENT,
            cursor="hand2"
        )

        register.pack(side="left")

        register.bind(
            "<Button-1>",
            lambda e: self.create_account()
        )

    # ========================================================
    # FOCUS DE EMAIL
    # ========================================================

    def email_focus_in(self, event=None):

        self.email_focused = True

        self.email_frame.config(
            bg="#293252"
        )

        self.email_icon.config(
            bg="#293252",
            fg=ACCENT
        )

        self.email_entry.config(
            bg="#293252"
        )

    def email_focus_out(self, event=None):

        self.email_focused = False

        self.email_frame.config(
            bg=INPUT_COLOR
        )

        self.email_icon.config(
            bg=INPUT_COLOR,
            fg=SECONDARY_TEXT
        )

        self.email_entry.config(
            bg=INPUT_COLOR
        )

    # ========================================================
    # FOCUS PASSWORD
    # ========================================================

    def password_focus_in(self, event=None):

        self.password_focused = True

        self.password_frame.config(
            bg="#293252"
        )

        self.password_icon.config(
            bg="#293252",
            fg=ACCENT
        )

        self.password_entry.config(
            bg="#293252"
        )

        self.show_password_button.config(
            bg="#293252"
        )

    def password_focus_out(self, event=None):

        self.password_focused = False

        self.password_frame.config(
            bg=INPUT_COLOR
        )

        self.password_icon.config(
            bg=INPUT_COLOR,
            fg=SECONDARY_TEXT
        )

        self.password_entry.config(
            bg=INPUT_COLOR
        )

        self.show_password_button.config(
            bg=INPUT_COLOR
        )

    # ========================================================
    # MOSTRAR / OCULTAR PASSWORD
    # ========================================================

    def toggle_password(self):

        self.password_visible = not self.password_visible

        if self.password_visible:
            self.password_entry.config(show="")
            self.show_password_button.config(text="○")
        else:
            self.password_entry.config(show="•")
            self.show_password_button.config(text="◉")

    # ========================================================
    # HOVER BOTÓN
    # ========================================================

    def login_hover(self, event=None):

        self.login_button.config(
            bg=ACCENT_HOVER
        )

    def login_leave(self, event=None):

        self.login_button.config(
            bg=ACCENT
        )

    # ========================================================
    # VALIDAR EMAIL
    # ========================================================

    def valid_email(self, email):

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        return re.match(pattern, email) is not None

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        # Limpiar errores anteriores
        self.clear_error()

        # Validar email
        if not email:

            self.show_error(
                "Introduce tu correo electrónico."
            )

            self.email_entry.focus()
            return

        if not self.valid_email(email):

            self.show_error(
                "El correo electrónico no es válido."
            )

            self.email_entry.focus()
            return

        # Validar contraseña
        if not password:

            self.show_error(
                "Introduce tu contraseña."
            )

            self.password_entry.focus()
            return

        if len(password) < 6:

            self.show_error(
                "La contraseña debe tener al menos 6 caracteres."
            )

            self.password_entry.focus()
            return

        # Simular login
        self.start_loading()

    # ========================================================
    # LOADING
    # ========================================================

    def start_loading(self):

        self.login_button.config(
            state="disabled",
            text="INICIANDO..."
        )

        self.after(
            1200,
            self.login_success
        )

    # ========================================================
    # LOGIN CORRECTO
    # ========================================================

    def login_success(self):

        self.login_button.config(
            state="normal",
            text="INICIAR SESIÓN"
        )

        self.show_success(
            "¡Inicio de sesión correcto!"
        )

        self.after(
            1500,
            self.open_dashboard
        )

    # ========================================================
    # DASHBOARD
    # ========================================================

    def open_dashboard(self):

        for widget in self.winfo_children():
            widget.destroy()

        dashboard = tk.Frame(
            self,
            bg=BG_COLOR
        )

        dashboard.pack(
            fill="both",
            expand=True
        )

        title = tk.Label(
            dashboard,
            text="✦  NOVA",
            font=("Arial", 30, "bold"),
            bg=BG_COLOR,
            fg=ACCENT
        )

        title.pack(pady=(180, 15))

        welcome = tk.Label(
            dashboard,
            text="Has iniciado sesión correctamente",
            font=("Arial", 22, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )

        welcome.pack()

        info = tk.Label(
            dashboard,
            text="Este sería tu panel principal.",
            font=("Arial", 11),
            bg=BG_COLOR,
            fg=SECONDARY_TEXT
        )

        info.pack(pady=10)

        logout = tk.Button(
            dashboard,
            text="Cerrar sesión",
            font=("Arial", 10, "bold"),
            bg=ACCENT,
            fg="white",
            activebackground=ACCENT_HOVER,
            border=0,
            cursor="hand2",
            padx=25,
            pady=10,
            command=self.restart
        )

        logout.pack(pady=25)

    # ========================================================
    # REINICIAR
    # ========================================================

    def restart(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.create_background()
        self.create_login_card()

    # ========================================================
    # MENSAJES DE ERROR
    # ========================================================

    def show_error(self, message):

        self.error_label = tk.Label(
            self.card,
            text=message,
            font=("Arial", 9),
            bg=CARD_COLOR,
            fg=ERROR_COLOR
        )

        self.error_label.pack(
            pady=(5, 0)
        )

        self.shake_window()

    def clear_error(self):

        if hasattr(self, "error_label"):
            self.error_label.destroy()
            del self.error_label

    # ========================================================
    # MENSAJE DE ÉXITO
    # ========================================================

    def show_success(self, message):

        self.clear_error()

        self.success_label = tk.Label(
            self.card,
            text=message,
            font=("Arial", 9, "bold"),
            bg=CARD_COLOR,
            fg=SUCCESS_COLOR
        )

        self.success_label.pack(
            pady=(8, 0)
        )

    # ========================================================
    # EFECTO SHAKE
    # ========================================================

    def shake_window(self):

        original_x = self.winfo_x()
        original_y = self.winfo_y()

        offsets = [
            -10, 10, -8, 8,
            -6, 6, -4, 4,
            -2, 2, 0
        ]

        def shake(index=0):

            if index >= len(offsets):
                self.geometry(
                    f"+{original_x}+{original_y}"
                )
                return

            x = original_x + offsets[index]

            self.geometry(
                f"+{x}+{original_y}"
            )

            self.after(
                30,
                lambda: shake(index + 1)
            )

        shake()

    # ========================================================
    # GOOGLE
    # ========================================================

    def google_login(self):

        messagebox.showinfo(
            "Google",
            "Aquí conectarías la autenticación real de Google."
        )

    # ========================================================
    # RECUPERAR CONTRASEÑA
    # ========================================================

    def forgot_password(self):

        messagebox.showinfo(
            "Recuperar contraseña",
            "Aquí podrías abrir una pantalla para recuperar "
            "la contraseña."
        )

    # ========================================================
    # CREAR CUENTA
    # ========================================================

    def create_account(self):

        messagebox.showinfo(
            "Crear cuenta",
            "Aquí podrías abrir el formulario de registro."
        )


# ============================================================
# EJECUTAR
# ============================================================

if __name__ == "__main__":

    app = LoginApp()

    app.mainloop()