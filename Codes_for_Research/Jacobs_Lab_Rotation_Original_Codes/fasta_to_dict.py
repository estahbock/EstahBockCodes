# Run this script first!!!!

# This script maps the peptides to the Rv numbers

# to run script, enter something like this: 
# python fasta_to_dict.py mycobacterium_tuberculosis_h37rv_2_proteins.fasta 6507_only_peptide.txt
# 6507_only_peptide.txt is a peptide list file

from sys import argv
script, File1, File2 = argv
from collections import defaultdict 

f = open(File1,'r')
list=defaultdict(str)
name = ''
peptides = open(File2,'r')
peptide_list = []
for line in peptides:
	line = line.strip()
	peptide_list.append(line)
#print(peptide_list) # sanity checking

# just made a list of the peptides
	
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    if line.startswith('>'):
    	line = line.split()
        name = line[2]
        continue #this means skips to the next line
    #This code is only executed if it is a sequence of bases and not a name.
    list[name]+=line.strip()
f.close()
# just converted protein fasta file to a dictionary (list)

#for gene in list.iterkeys(): # sanity checking
#	print(gene)
#	print(list[gene])

# making peptide hit dictionary and printing results:

pep_hit_dict = {}

for peptide in peptide_list:
	for gene in list.iterkeys():
		if list[gene].find(peptide) != -1: # if peptide is in the protein:
			if peptide not in pep_hit_dict: # and it is not in the dictionary
				gene_list = []
				gene_list.append(gene)
				pep_hit_dict[peptide] = gene_list # puts it in the dictionary
			else:
				pep_hit_dict[peptide] = gene_list # if it is in the dictionary (more than one hit)
				gene_list.append(gene) # updates the dictionary accordingly
				#print pep_hit_dict[peptide]
				#print peptide
	if peptide not in pep_hit_dict: # if the peptide has no hits:
		pep_hit_dict[peptide] = 0 # puts it in the dictionary with a value of 0
		print '#' + ' ' + peptide # and prints "#" and the peptide
	else: # if the peptide has hits,
		if len(pep_hit_dict[peptide]) > 1: # and it has more than one hit:
			print '#' + ' ' + peptide # prints "#" and the peptide
			print pep_hit_dict[peptide][0] # prints the first hit
			i = 0
			while i < len(pep_hit_dict[peptide]):
				print '#' + ' ' + pep_hit_dict[peptide][i]
				i += 1 # prints "#" followed by a hit (does for each hit)
		else: # if there is only one hit (or it has one hit, 0 value in dict)
			if pep_hit_dict[peptide] != 0: # and the value is not 0 (actually has a hit):
				print pep_hit_dict[peptide][0] # prints the hit
			
#print pep_hit_dict sanity checking

# just went through the list of peptides and searched for the peptides, one by one,
# in each protein entry and printed hits (after printing the peptide)

# note: some peptides have multiple hits and some peptides have no hits

# This script to convert the fasta file to a dict is derived from answer on stack overflow: 
# http://stackoverflow.com/questions/22698807/parse-fasta-sequence-to-the-dictionary