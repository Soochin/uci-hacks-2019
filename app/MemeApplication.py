import tkinter

class MemeApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._create_canvas()

    def _create_canvas(self):
        self._canvas = tkinter.Canvas(master = self._root_window, width=200, height=200)
    
    def run(self):
        self._root_window.mainloop()