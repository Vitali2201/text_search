import os

class Library:

	def __init__(self, words):
		self.words = words
		
		self.files = self.list_of_books()
		self.result = self.book_search()
		

	def list_of_books(self):
		directory = '/home/vital/Загрузки/books'
		self.files = os.listdir(directory)
		return self.files

	def book_search(self):
		for filename in self.files:
			with open(filename, 'r', encoding='Windows-1251') as f:
				for line in f:
					if self.words in line:
						self.filename = filename
						self.line = line
						return self.filename

	def recording(self):
		with open('result.txt', 'a') as f:
			f.write(f'{self.filename}\n{self.line}\n')
		
									
d = Library('наблюдатель')

d.recording()


# words = 'наблюдатель'

# directory = '/home/vital/Загрузки/books'
# files = os.listdir(directory)
# for filename in files:
# 	with open(filename, 'r', encoding='Windows-1251') as f:
# 		for line in f:
# 			if words in line:
# 				with open('result.txt', 'a') as f:
# 					f.write(f'{filename}\n{line}\n')
# 			else:
# 			 	None
