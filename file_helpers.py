def file_read():
##    with open('lookups.txt', 'r') as f:
##        file_contents = f.read()
##        return file_contents
    with open('lookups.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
        return data
    

def file_edit(edit):
    with open("lookups.txt", "w") as f:
        f.write(edit)

