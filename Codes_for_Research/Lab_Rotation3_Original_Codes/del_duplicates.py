# Run this script third!!!!

# This script removes duplicates and makes sure every hit is in the correct list
# it also notes which peptides have multiple hits or no hits

# to run script, enter something like this: 
# python del_duplicates.py 6230_Rv_from_pep.txt 6507_Rv_from_pep.txt common_peptides_mapped.txt
# python del_duplicates.py sample_Rv_annot2.txt sample_Rv_annot.txt sample_Rv_annot_common.txt
# For this to show correct information, you need to have the 6230 file, then 6507 file, 
# then common file

from sys import argv
script, File1, File2, File3 = argv
import re

f1 = open(File1,'r')

print "6230 no or multiple hits:"

Rv_dict_1 = {}
Rv_list_1 = []
for line in f1:
    line = line.strip()
    if line.startswith('Rv'):
    	line_parts = re.split(r'\t+', line)
    	if line_parts[0] in Rv_list_1:
    		#print line_parts[0]
    		pass
    	else:
    		Rv_dict_1[line_parts[0]] = line_parts
    		Rv_list_1.append(line_parts[0])
    		#print '\t'.join(map(str, Rv_dict_1[line_parts[0]]))
    		pass
    elif line.startswith('#'):
    	print line # prints all commented lines (multiple or no hits)
    else:
    	pass

f1.close()
# made list of 6230 hits and made 6230 hits dictionary (removes duplicates by default)

f2 = open(File2,'r')

print "6507 no or multiple hits:"

Rv_dict_2 = {}
Rv_list_2 = []
for line in f2:
    line = line.strip()
    if line.startswith('Rv'):
    	line_parts = re.split(r'\t+', line)
    	if line_parts[0] in Rv_list_2:
    		#print line_parts[0]
    		pass
    	else:
    		Rv_dict_2[line_parts[0]] = line_parts
    		Rv_list_2.append(line_parts[0])
    		#print '\t'.join(map(str, Rv_dict_2[line_parts[0]]))
    		pass
    elif line.startswith('#'):
    	print line  # prints all commented lines (multiple or no hits)
    else:
    	pass

f2.close()
# made list of 6507 hits and made 6507 hits dictionary (removes duplicates by default)

f3 = open(File3,'r')

print "common no or multiple hits:"

common_list = []
for line in f3:
    line = line.strip()
    if line.startswith('Rv'):
    	line_parts = re.split(r'\t+', line)
    	if line_parts[0] in common_list:
    		#print line_parts[0]
    		pass
    	else:
    		common_list.append(line_parts[0])
    		pass
    elif line.startswith('#'): # prints all commented lines (multiple or no hits)
    	print line
    else:
    	pass
f3.close()
# made list of common hits (removes duplicates by default)

# Need to update if certain hits should be in the common list and removed from unique lists:
# Also need to print final version: 

print "6230 unique:"
for Rv in Rv_list_1:
	if Rv not in Rv_list_2:
		if Rv not in common_list:
			print '\t'.join(map(str,Rv_dict_1[Rv]))
			#print Rv
	else:
		if Rv not in common_list:
			common_list.append(Rv)
print "6507 unique:"
for Rv in Rv_list_2:
	if Rv not in Rv_list_1:
		if Rv not in common_list:
			print '\t'.join(map(str,Rv_dict_2[Rv]))
			#print Rv
	else:
		if Rv not in common_list:
			common_list.append(Rv)

print "Common:"
for Rv in common_list:
	print Rv
		
		
		