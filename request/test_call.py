import os
import json
from books import call

results = call(q= 'Johannes_Cabal',
               printType= 'books',
               key= os.environ['GB_KEY'])

file = open('result.json', 'w')
json.dump(results, file)
file.close()

print(results)
