'''
Created on: 10/7/2024

@author: sacuervo
'''


class View:

    def __init__(self, controller):
        self.controller = controller

    def main(self):
        print("In main of view")