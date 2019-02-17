import tkinter
import meme
from PIL import Image, ImageTk

DEFAULT_FONT = ('Helvetica', 30)

class MemeApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.title("Gimme a Dog!!!")
        self._root_window.geometry("600x600")

        self._button = tkinter.Button(master=self._root_window, text="Doggo Waiting V'ㅈ'V",
                                      font=DEFAULT_FONT,
                                      command=self._on_button_clicked, height=10)

        # self._canvas = tkinter.Canvas(master = self._root_window, width=500, height=500)
        # self._canvas.grid(row=0, column=0, padx=10, pady=10,
        #                  sticky=tkinter.N + tkinter.S)
        self._button.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky=tkinter.N)


    def _on_button_clicked(self) -> None:
        print("Clicked")
        img = meme.get_meme()
        text = meme.pick_title()

        tkimage = ImageTk.PhotoImage(img)
        label = tkinter.Label(self._root_window, image=tkimage,
                              text=text, compound=tkinter.CENTER)
        label.grid(row=0, column=0, padx=10, pady=10)
    
    def run(self):
        self._root_window.mainloop()