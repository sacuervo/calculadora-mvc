'''
Created on: 10/7/2024

@author: sacuervo
'''

import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("IberoCalc")
        self._make_main_frame()
        self._make_entry()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(self.main_frm)

