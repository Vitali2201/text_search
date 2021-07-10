import urllib.request

import chardet 

data = urllib.request.urlopen('/home/vital/Загрузки/books/library/')
chardet.detect(rawdata.read())
