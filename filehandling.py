'''
Github: https://github.com/kormin
Description: File Handling
Created On: 2016
Additional Comments: 
This is a python 3 implementation.
'''

class fileHandle():
	def __init__(self, filename):
		self.filename = filename

	def read(self):
		file = open(self.filename, 'r')
		self.contents = file.read()
		# print(self.contents)
		file.close()

	def getContents(self):
		return self.contents

	def dispList(self, list, length):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(list)))
		print("Length: ",(length))

link = fileHandle("notes.txt")
link.read()
linkval = link.getContents()
print(linkval)
