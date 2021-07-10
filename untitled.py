import os

words = 'наблюдатель'

directory = '/home/vital/Загрузки/books'
files = os.listdir(directory)
for filename in files:
	with open(filename, 'r', encoding='Windows-1251') as f:
		try:
			open(filename, 'r')
		except UnicodeDecodeError:
			open(filename, 'r', encoding='utf-8')
		for line in f:
			if words in line:
				with open('result.txt', 'a') as f:
					f.write(f'{filename}\n{line}\n')
			else:
			 	None
	