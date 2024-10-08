'''
Created on: 10/7/2024

@author: sacuervo
'''

from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model() # Conectar el modelo
        self.view = View(self) # Conectar la vista pasándose a sí mismo como argumento

    def main(self):
        self.view.main()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()