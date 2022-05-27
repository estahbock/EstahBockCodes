

# to run this python script type: python make_file_gi_Rv.py gi_list.txt end_file.txt
from sys import argv
import re

script, File1, File2 = argv

def command_list(file, line_made):
	file1 = open(file)
	
	for line in file1:
		line = line.strip()
		line2 = re.split(r'\|+', line)
		this_out = "grep %s Bacteria.gene_info \n"%line2[1]
		#print(this_out)
		output.append(this_out)
		#print(line)
		
	file1.close()
output = []
command_list(File1, output)


outfile = open(File2, 'w')
outfile.writelines(output)
outfile.close()

 
