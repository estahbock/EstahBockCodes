# Run this script second!

# This script puts the gene annotations, 

# to run script, enter something like this into terminal: 
# python find_Rv_in_dict.py 6230_peptides_mapping.txt mycobacterium_tuberculosis_h37rv_2_genome_summary_per_gene.txt
# 6230_peptides_mapping.txt is the text file made by pasting the terminal output of 
# fasta_to_dict.txt

from sys import argv
script, File1, File2 = argv

import re

Rv_dict = {}

f2 = open(File2,'r')
for line in f2:
    line = line.strip()
    line_parts = re.split(r'\t+', line)
    Rv_dict[line_parts[0]] = line_parts
f2.close()

# just converted genome summary file entries into dictionary, with Rv number key

# for i in Rv_dict.iterkeys(): # sanity checking (printing dictionary)
# 	print '\t'.join(map(str, Rv_dict[i][0:len(Rv_dict[i])]))


f1 = open(File1,'r')
	
for line in f1:
    line = line.strip()
    if line.startswith('Rv'):
    	line_parts = line.split()
    	print '\t'.join(map(str, Rv_dict[line_parts[0]]))
    else:
    	print line
f1.close()

# just printed all lines of the old file except where the Rv number hit is, the whole
# dict entry for that Rv number was printed 
# see output in terminal. Copy and paste to a new txt file