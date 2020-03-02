import tkinter as tk

from orca.component import Component
from orca.state import State

from .components.Counter.main import Counter

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

        count.pack(expand=True, fill="both")
        
        return locals()


