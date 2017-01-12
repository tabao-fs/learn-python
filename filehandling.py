'''
Github: https://github.com/kormin
Description: File Handling
Created On: 2016
Additional Comments: 
This is a python 3 implementation.
'''

class FileHandle():
	def __init__(self, filename):
		self.filename = filename

	def read(self):
		file = open(self.filename, 'r')
		self.contents = file.read()
		# print(self.contents)
		file.close()

	def write(self, contents):
		file = open(self.filename, 'w')
		file.write(contents)
		file.close()

	def setFilename(self, filename):
		self.filename = filename

	def getContents(self):
		return self.contents

	def dispList(self, list, length):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(list)))
		print("Length: ",(length))

link = FileHandle("notes.txt")
link.read()
linkval = link.getContents()

# track = FileHandle(linkval)
# track.read()
# trackval = track.getContents()
# track.setFilename("list.txt")
# track.write(trackval)
