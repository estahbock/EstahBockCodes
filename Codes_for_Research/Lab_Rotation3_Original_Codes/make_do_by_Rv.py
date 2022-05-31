# to run script, enter something like this: 
# python make_do_by_Rv.py 6230_peptides_mapping.txt
from sys import argv
script, File1 = argv

f = open(File1,'r')
	
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    line = line.strip()
    if line.startswith('Rv'):
    	this_out = "grep %s mycobacterium_tuberculosis_h37rv_2_genome_summary_per_gene.txt"%line
    	print(this_out)
    else:
    	print "echo \#%s"%line
f.close()