import tkinter as tk
from core.component import Component
from core.state import State

from .style import style


class Counter(Component):

    def __init__(self, root, number):

        self.number = number

        super().__init__(root, state=State({
            'click': 0
        }))


    def render(self):
        if self.state.click < self.number:
            lbl = tk.Label(self, text=f"Clicks made: {self.state.click}", bg=self.root.state.bg)
            lbl.pack(fill="x")

            btn = tk.Button(self, text="Click Me", command= self.command)
            btn.pack(side="left", fill="y")
            btn.configure(style.btn if self.state.click >= self.number/2 else {})
        else: 
            lbl2 = tk.Label(self, text="Fuck yeah", bg=self.root.state.bg)
            lbl2.pack()

            close = tk.Button(self, text="Close", command= self.root.root.destroy)
            close.pack()

        
        if self.state.click >= self.number:
            self.root.state.set_state({'bg': '#a8b4e5'}) 
        return locals()


    def command(self):
        self.state.set_state({'click': self.state.click+1})