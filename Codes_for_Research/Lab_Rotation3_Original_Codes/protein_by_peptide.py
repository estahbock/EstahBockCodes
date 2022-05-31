# goal: make script that makes do file that looks this:
# echo PEPTIDE
# grep -C 10 PEPTIDE mycobacterium_tuberculosis_h37rv_2_proteins.fasta

# to run this python script type: python protein_by_peptide.py peptide_list.txt
from sys import argv

script, File1 = argv

def peptide_list(file, out):
	file1 = open(file)
	
	for line in file1:
		line = line.strip()
		#print(line)
		#line = line.split() #needed along with while i < len(output[0]): and output[0][i]
		output.append(line)
		#print ">%d"%i
		#print(line)
		
	file1.close()
	
output = []	
peptide_list(File1, output)

print len(output[0])

i = 1
while i < len(output):
	print "echo peptide%s"%output[i]
	print "grep -B 5 %s mycobacterium_tuberculosis_h37rv_2_proteins.fasta"%output[i]
	i = i + 1
