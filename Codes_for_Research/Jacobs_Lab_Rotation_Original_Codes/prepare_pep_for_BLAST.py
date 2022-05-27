
# to run this python script type: python make_file_gi_Rv.py gi_list.txt end_file.txt
from sys import argv


script, File1 = argv

def peptide_list(file, out):
	file1 = open(file)
	
	for line in file1:
		line = line.strip()
		line = line.split()
		output.append(line)
		#print ">%d"%i
		#print(line)
		
	file1.close()
	
output = []	
peptide_list(File1, output)

print len(output[0])

i = 1
while i < len(output[0]):
	print ">%d"%i
	print(output[0][i])
	i = i + 1
	