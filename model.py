'''
Created on: 10/7/2024

@author: sacuervo
'''

# El modelo maneja la lógica de cálculo de la calculadora
class Model:

    def __init__(self):
        self.previous_value = ''  # Valor previo para realizar las operaciones
        self.value = ''  # Valor actual ingresado
        self.operator = ''  # Operador seleccionado (+, -, /, *)

    # Método que calcula el resultado en base a los botones presionados
    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''  # Reinicia la calculadora
        elif isinstance(caption, int):
            self.value += str(caption)  # Agrega números al valor actual
        elif caption == "+/-":
            # Invierte el signo del valor actual
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == '%':
            pass  # Aún no implementado
        elif caption == "=":
            self.value = str(self._evaluate())  # Realiza la operación al presionar "="
        elif caption == '.':
            if '.' not in self.value:
                self.value += caption  # Agrega el punto decimal si no está presente
        else:
            if self.value:
                self.operator = caption  # Guarda el operador
                self.previous_value = self.value  # Guarda el valor previo
                self.value = ''  # Resetea el valor actual

        return self.value  # Retorna el valor actualizado

    # Método auxiliar que realiza la operación matemática
    def _evaluate(self):
        # Asegura que no se realice una división por cero
        if self.operator == '/' and eval(self.previous_value + '%' + self.value) == 0:
            self.operator = "//"  # Evita la división por cero
        return eval(self.previous_value + self.operator + self.value)  # Evalúa la expresión matemática
