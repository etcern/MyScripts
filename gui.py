import threading
import tkinter as tk
from sys import exit

root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("300x300+50+50")

# Create two labels
tk.Label(root, text="").pack()
tk.Label(root, text="").pack()
tk.Label(root, text="").pack()
tk.Label(root, text="Press F8 to start / stop the macro").pack()
status_label = tk.Label(root, text="Current Toggle state: " + str(False))
status_label.pack()
def on_closing():
        quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
def run_gui():
    threading.Thread(target=root.mainloop, daemon=True).start()