import os


class Library:

    def __init__(self, words):
        self.words = words
        self.result_list = []

        self.files = self.list_of_books()
        self.book_search()

    def list_of_books(self):
        directory = '/home/vital/Загрузки/books/library'
        self.files = os.listdir(directory)
        return self.files

    def book_search(self):
        for filename in self.files:
            with open(filename, 'r', encoding='Windows-1251') as f:
                for line in f:
                    if self.words in line:
                        self.result_list.append(f'{filename}')

    def recording(self):
        with open('result.txt', 'a') as f:
            f.write(f'{(",".join(self.result_list))}'.replace(",", "\n"))


d = Library('наблюдатель')

d.recording()
