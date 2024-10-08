from model import Model
from view import View

# El controlador actúa como intermediario entre el modelo y la vista
class Controller:

    def __init__(self):
        self.model = Model()  # Conectar el modelo
        self.view = View(self)  # Conectar la vista, pasándose a sí mismo como argumento

    # Método principal que inicia la vista
    def main(self):
        self.view.main()

    # Método que se llama cuando un botón de la vista es presionado
    def on_button_click(self, caption):
        result = self.model.calculate(caption)  # Pasa la acción al modelo para que lo calcule

        self.view.value_var.set(result)  # Actualiza la pantalla de la calculadora con el resultado


if __name__ == '__main__':
    calculator = Controller()  # Instancia el controlador
    calculator.main()  # Inicia la aplicación
