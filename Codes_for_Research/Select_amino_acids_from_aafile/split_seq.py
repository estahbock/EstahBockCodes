# This used to help get the amino acids of a select range 
# in a protein sequence (aa1 - aa2)
from sys import argv

script, File1, File2, aa1, aa2 = argv

target = open(File2, 'w')

for line in open(File1):
	aa_list1 = str(line)
	start = int(aa1) - 1
	end = int(aa2)
	aa = aa_list1[start:end]
	
	target.write(aa)
	print aa


    
target.close()