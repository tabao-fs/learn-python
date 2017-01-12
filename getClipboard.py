'''
Github: https://github.com/kormin
Description: Copies string to clipboard and waits for paste
Created On: 2016
Additional Comments: 
This is a python 3 implementation.
'''

from tkinter import Tk

class Clipboard:
	def __init__(self, contents):
		self.contents = contents

	def copy(self):
		r = Tk()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(self.contents)
		self.wait()
		r.destroy()

	def wait(self):
		input("Press Enter to continue...")

# 	def close(self):
# 		self.r.destroy()

cb = Clipboard("hello world")
cb.copy()
# cb.wait()
# cb.close()

# contents = "hello world"
# r = Tk()
# r.withdraw()
# r.clipboard_clear()
# r.clipboard_append(contents)
# input("Press Enter to continue...")
# r.destroy()