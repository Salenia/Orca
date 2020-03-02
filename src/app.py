import tkinter as tk

from core.component import Component
from core.state import State

from .components.Counter.main import Counter
from .components.test import Woe

class App(Component):

    def __init__(self, root):

        super().__init__(root, state=State({
            'bg': root['bg']
        }))

    def render(self):

        header = tk.Label(self, text="My Cool Reactive App", font=('',14, 'bold'),
        bg= self.state.bg)
        header.pack(fill="x")

        count = Counter(self, number=4)
        count['bg']= self.state.bg
        #print(f'{count = }')
        count.pack(expand=True, fill="both")
        
        return locals()


