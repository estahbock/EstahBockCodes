# To run, type the following
# python QC1.py testimaris.txt
from sys import argv

script, File1 = argv

# Use testimaris.txt for File1
# Use QC1.py for script

f1 = open(File1, 'r')

def turn_into_dict(d1):
	for line in f1:
		if not line.startswith('#'):						# goes through line by line
			# ignores lines that start with a "#"
			# !will need to add in miniscript that adds "#" to front of first 2 rows!
			#print line										# command to check script
			(clusterindex_protein, clusterindex_rna, area, perimeter, shape_factor, spot_count_CY5, 
			spot_area_avrg_CY5, spot_diameter_avrg_CY5, spot_count_TRITC, spot_area_avrg_TRITC, 
			spot_diameter_avrg_TRITC, max_fusion_distance_protein, spot_count_protein, 
			cell_ID) = line.split("\t")
			key = "%d" % float(cell_ID)
			#print key
			l = [clusterindex_protein, clusterindex_rna]
			#print l
			d1[key] = l
			

dict_made = {}											# makes empty dict.
turn_into_dict(dict_made)								# command to use dict-making 
														# function.
#print dict_made										# command to check script
rna_and_protein_detected = []
rna_only_detected = []
protein_only_detected = []
cells_negative = []
any_rna = []
any_protein = []

for a in dict_made.iterkeys():							# makes for loop to go through 
														# each key1 (geneID) in the dict.
		#print str(a)
		l1 = dict_made[a][0]							# l1 is from clusterindex_protein
		#print l1
		l2 = dict_made[a][1]							# l2 is from clusterindex_rna
		#print l2
		
		if l1 != "Empty Nuclei" and l2 != "Empty Nuclei":
			rna_and_protein_detected.append(a)
			any_rna.append(a)
			any_protein.append(a)
		if l1 != "Empty Nuclei" and l2 == "Empty Nuclei":
			protein_only_detected.append(a)
			any_protein.append(a)
		if l1 == "Empty Nuclei" and l2 != "Empty Nuclei":
			rna_only_detected.append(a)
			any_rna.append(a)	
		if l1 == "Empty Nuclei" and l2 == "Empty Nuclei":
			cells_negative.append(a)


rna_and_protein_detected.sort(key=int)
protein_only_detected.sort(key=int)
rna_only_detected.sort(key=int)
any_rna.sort(key=int)
any_protein.sort(key=int)

cells_detected = len(rna_only_detected) + len(protein_only_detected) 
cells_detected += len(rna_and_protein_detected) + len(cells_negative)

print "%d cells detected" % cells_detected

print "%d cells with RNA_A and ProteinA Detected" % len(rna_and_protein_detected)
print "\t".join(rna_and_protein_detected)
i = 0
number_for_rna_and_protein = []
while len(rna_and_protein_detected) > i:
	number_for_rna_and_protein.append(str(i+1))
	i += 1
print "\t".join(number_for_rna_and_protein)

print "%d cells with only RNA_A Detected" % len(rna_only_detected)
print "%d cells with RNA_A Detected" % len(any_rna)
print "\t".join(any_rna)
i = 0
number_for_rna = []
while len(any_rna) > i:
	number_for_rna.append(str(i+1))
	i += 1
print "\t".join(number_for_rna)

print "%d cells with only ProteinA Detected" % len(protein_only_detected)
print "%d cells with ProteinA Detected" % len(any_protein)
print "\t".join(any_protein)
i = 0
number_for_ProteinA = []
while len(any_protein) > i:
	number_for_ProteinA.append(str(i+1))
	i += 1
print "\t".join(number_for_ProteinA)
	
f1.close()
