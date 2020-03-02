import tkinter as tk 
from app import App

if __name__ == "__main__":
    root = tk.Tk()  
    root.geometry('450x300')

    app = App(root)
    app.pack(expand=True, fill="both")
    app['bg'] = 'blue'

    root.mainloop()