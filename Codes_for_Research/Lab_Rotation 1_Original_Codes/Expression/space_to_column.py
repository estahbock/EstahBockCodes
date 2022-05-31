# This used to help get data pasted directly from a PDF file
from sys import argv

script, File1, File2 = argv

target = open(File2, 'w')

for line in open(File1):
	a = line.split()
	for gene in a:
		if any(x.isalpha() for x in gene):
			target.write(gene)
			target.write("\n")
			print gene
# still have to delete last line in new txt file
    
target.close()