import os

import os
def listFiles(path):
    #from notes
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [os.path.abspath('.') + "/" + path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

# file = listFiles("Files")
# file1 = open(file[0])
# contents = file1.read()
# print(file)
# file1.close()
#print(contents)
save2 = open('Save9', 'w')
save2.write("hi")
save2.close()
# file2 = open('/Users/rollingstudent/Desktop/TP3/Save2')
# contents2 = file2.read()
# print(contents2)

