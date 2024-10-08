'''
Created on: 10/7/2024

@author: sacuervo
'''


class Model:

    def __init__(self):

        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif isinstance(caption, int):
            self.value += str(caption)

        elif caption == "+/-":
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            pass

        elif caption == "=":
            self.value = str(self._evaluate())

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        if self.operator == '/' and eval(self.previous_value + '%' + self.value) == 0:
            self.operator = "//"
        return eval(self.previous_value + self.operator + self.value)
