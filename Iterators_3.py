def word_finder(file_name):
    for row in open(file_name, "r"):
        yield row

word_found = False

obj = word_finder('my_file.txt')

for row in obj:
    
    if 'name' in row:
        word_found = True
        break
    else:
        continue

if word_found:
    print('Word Found In The File!')
else:
    print('Word Not Found In File!')
    
    
    
    




