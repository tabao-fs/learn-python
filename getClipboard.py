'''
Github: https://github.com/kormin
Description: Copies string to clipboard and waits for paste
Created On: 2016
Additional Comments: 
This is a python 3 implementation.
'''
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('clipboard')
# print(r.clipboard_get())
# val = ''
# while (val!='\n'):
	# val = input("Press [enter] to end program: ")
input("Press Enter to continue...")
r.destroy()