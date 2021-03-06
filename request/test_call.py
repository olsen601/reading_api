import os
import json
from books import call

results = call(q= 'Johannes_Cabal',
               printType= 'books',
               key= os.environ['GB_KEY'],
               fields="kind,items(id,selfLink,volumeInfo/title,volumeInfo/authors,volumeInfo/publishedDate,volumeInfo/description,volumeInfo/industryIdentifiers,volumeInfo/categories,volumeInfo/imageLinks/smallThumbnail)")

file = open('result.json', 'w')
json.dump(results, file)
file.close()

print(results)
