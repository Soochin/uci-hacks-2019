import tkinter
import meme

DEFAULT_FONT = ('Helvetica', 30)

class MemeApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.title("Gimme a Dog!!!")
        self._root_window.geometry("300x300")

        self._button = tkinter.Button(master=self._root_window, text="Doggo Waiting V'ㅈ'V",
                                      font=DEFAULT_FONT,
                                      command=self._on_button_clicked, height=10)
        self._button.pack()

    def _on_button_clicked(self) -> None:
        print("Clicked")
        meme.show_meme()
    
    def run(self):
        self._root_window.mainloop()