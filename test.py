import tkinter as tk

class MyWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ma fenêtre")
        self.geometry("200x200")

        # Maintient la fenêtre au premier plan
        self.attributes("-topmost", True)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    # Crée deux fenêtres qui se superposent
    win1 = MyWindow(root)
    win2 = MyWindow(win1)

    root.mainloop()
