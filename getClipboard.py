from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('clipboard')
print(r.clipboard_get())
r.destroy()