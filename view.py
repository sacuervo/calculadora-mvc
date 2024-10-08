import tkinter as tk
from tkinter import ttk

# La clase View maneja la interfaz gráfica de la calculadora usando Tkinter
class View(tk.Tk):
    PAD = 10  # Constante que establece el padding entre elementos de la interfaz
    MAX_BUTTONS_PER_ROW = 4  # Número máximo de botones por fila

    # Definición de los botones de la calculadora, incluyendo operadores y números
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '=',
    ]

    def __init__(self, controller):
        super().__init__()  # Llama al constructor de la clase Tk
        self.title("IberoCalc")  # Establece el título de la ventana
        self.config(bg='#000')  # Configura el fondo de la ventana
        self.controller = controller  # Guarda la referencia al controlador
        self.value_var = tk.StringVar()  # Variable para mostrar el valor actual de la calculadora

        self._configure_button_styles()  # Configura los estilos de los botones
        self._make_main_frame()  # Crea el marco principal de la interfaz
        self._make_label()  # Crea la etiqueta donde se muestran los resultados
        self._make_buttons()  # Crea los botones de la calculadora
        self._center_window()  # Centra la ventana en la pantalla

    # Método que configura los estilos de los botones
    def _configure_button_styles(self):
        style = ttk.Style()
        style.theme_use('alt')

        # Estilo para botones numéricos
        style.configure('N.TButton', foreground='white', background='gray')

        # Estilo para botones de operadores
        style.configure('O.TButton', foreground='white', background='orange')

        # Estilo para el resto de botones
        style.configure('R.TButton', background='white')

    # Método principal para iniciar el ciclo de eventos de la ventana
    def main(self):
        self.mainloop()

    # Crea el marco principal donde se posicionan los demás elementos
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    # Crea la etiqueta que muestra el valor en la pantalla de la calculadora
    def _make_label(self):
        lbl = tk.Label(self.main_frm, anchor='e', textvariable=self.value_var, background="#000", foreground="#fff",
                       font=('Arial', 30))
        lbl.pack(fill='x')

    # Método que crea los botones de la calculadora
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        is_first_row = True
        buttons_in_row = 0

        # Recorre los captions de los botones y los posiciona
        for caption in self.button_captions:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x')
                is_first_row = False
                buttons_in_row = 0

            # Asigna estilos según si es un número, operador o botón especial
            if isinstance(caption, int):
                style_prefix = 'N'  # Estilo para números
            elif self._is_operator(caption):
                style_prefix = 'O'  # Estilo para operadores
            else:
                style_prefix = 'R'  # Estilo para otros botones

            style_name = f'{style_prefix}.TButton'

            # Crea el botón y asigna la acción correspondiente
            btn = ttk.Button(
                frm,
                text=caption,
                command=(lambda button=caption: self.controller.on_button_click(button)),
                width=20,
                style=style_name
            )

            # Ajusta el tamaño de los botones según el tipo (ej. el botón "0" es más ancho)
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0

            btn.pack(fill=fill, expand=expand, side='left')

            buttons_in_row += 1

    # Método auxiliar que determina si el botón es un operador
    def _is_operator(self, button_caption):
        return button_caption in ['/', '*', '+', '-', '=']

    # Centra la ventana en la pantalla
    def _center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
