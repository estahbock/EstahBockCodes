# This script gets rid of blank lines in the text file
from sys import argv

script, file1, file2 = argv

target = open(file2, 'w')

for line in open(file1):
  line = line.rstrip()
  if line != '':
    print line
    target.write(line)
    target.write("\n")
# still have to delete last line in new txt file
    
target.close()
