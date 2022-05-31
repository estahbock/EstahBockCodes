from sys import argv

script, File1 = argv

# Use metafile_alt_splicing_2.txt for File1

filelist = open(File1)

# reading file list from metafile:
file_list = []
for line in filelist:
	file_list.append(line.rstrip("\n"))
#print file_list 										# command to check script

filelist.close()

# making a function to turn the data into a 2D dictionary
def turn_into_dict(x, dict_made):
	G = len(x)											# G is # of files used
	i = 0 												# counter for file # 
														# (starts with 0 for first)
	while i < G: 										# and stops when out of files.
		
		FILE_X = open(x[i])								# item in file list based 
														# on counter
		
		for line in FILE_X:
			if not line.startswith('#'):				# goes through line by line
			# ignores lines that start with a "#"
				(geneID, exon, gene_name, padjust, log2FC) = line.split()
				# split line into the above variables
				# This is a 2D dict, thus need assign 2 keys:
				key1 = "geneID: %s gene name: %s" % (geneID, gene_name) 
				key2 = "exon: %s" % exon
				# key1 is geneID and gene name because the first grouping is by gene.
				# key2 is exon because the gene is further divided by the exon #
				padjust = float(padjust)				# makes sure padjust and log2FC
				log2FC = float(log2FC)					# are numbers for later cutoffs,
														# if desired
				FC = (2 ** log2FC)						# converting to fold change (FC)
				#print FC
				# if statement to do different things depending on if key1 (geneID) 
				# and key2 (exon) is in the dict, just key1 is in the dict, or 
				# neither keys are in the dict
				# Structured so there are 3 columns of FC, then 3 columns of padjust
				# This part is for if both keys are in the dict:
				if key1 in dict_made and key2 in dict_made[key1]:
					dict_made[key1][key2][i] = FC	# puts FC in correct location
					j = G + i
					dict_made[key1][key2][j] = padjust	# puts padjust in correct location
					#print key1, key2, dict_made[key1][key2] # command to check script
				# This part is for if key1 (geneID) is in the dict by key2 (exon) is not:
				elif key1 in dict_made and (key2 not in dict_made):
					val_list = []						# val_list is list of FC and
														# padjust for each comparison
					# k is a counter for the location in val_list the script is at.
					k = 0
					while k < i:						# puts 1 placeholders up until
						val_list.append(1)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(FC)					# puts FC in correct location.
					k += 1
					while k < G:						# puts 1 placeholders up until
						val_list.append(1)				# the end of the length of the
						k += 1							# file list.
					while k < (i + G):					# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at plus the
														# length of the list
					val_list.append(padjust)			# puts padjust in correct location
					k += 1
					while k < (G + G):					# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
						k += 1							# file list times 2.
					dict_made[key1][key2] = val_list	# a dict entry is made with 
														# val_list.
				# This part is for if key1 is not in the dict:
				else:
					dict_made[key1] = {}
					val_list = []
					# k is a counter for the location in val_list the script is at.
					k = 0
					while k < i:						# puts 1 placeholders up until
						val_list.append(1)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(FC)					# puts FC in correct location
					k += 1
					while k < G:						# puts 1 placeholders up until
						val_list.append(1)				# the end of the length of the
						k += 1							# file list.
					while k < (i + G):					# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at plus the
														# length of the list
					val_list.append(padjust)			# puts padjust in correct location
					k += 1
					while k < (G + G):					# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
						k += 1							# file list times 2.
					dict_made[key1][key2] = val_list	# a dict entry is made with 
														# val_list.
					#print key1, key2, dict_made[key1][key2] # command to check script
		FILE_X.close()
		i += 1											# moves on to next file

all_files_dict = {}										# makes empty dict.
turn_into_dict(file_list, all_files_dict)				# command to use dict-making 
														# function.
#print all_files_dict 									# command to check script

print "Full table:"

def readout(k1, d):										# creates function to make a
														# readout.
	print str(k1)										# prints key1.
	for b in d[k1].iterkeys():
		print ' ', str(b), ' '.join(map(str, d[k1][b]))	# prints key2 under those under 
														# key1 along with values for each.

for a in all_files_dict.iterkeys():						# makes for loop to go through 
														# each key1 (geneID) in the dict.
	readout(a, all_files_dict)							# performs readout function to 
														# print each grouped dict entry
														# in an organized manner

# The following is code to compare the data from the different files through
# separating into groups based on the comparison:
					
print "Comparisons:"

# making a function to compare the data of different files through making group using 
# each gene fed through this function using one of the commands that follows:

def compare_files(inc, dcr, pv, gene, d2):							# uses gene fed through
														# and dictionary made earlier.
	for c in d2[gene].iterkeys():						# goes through each exonID for 
														# the gene.
		l2 = all_files_dict[gene][c][0]					# l2 is the Treatment2 FC
		l3 = all_files_dict[gene][c][1]					# l3 is the Treatment3 FC
		l4 = all_files_dict[gene][c][2]					# l4 is the Treatment4 FC
		p2 = all_files_dict[gene][c][3]					# p2 is the Treatment2 padjust
		p3 = all_files_dict[gene][c][4]					# p3 is the Treatment3 padjust
		p4 = all_files_dict[gene][c][5]					# p4 is the Treatment4 padjust

		#### asks for inputs on pvalue cutoff and FC cutoff later in script
		val = '%s %s %s %s %s %s %s %s' % (gene, c, l2,l3, l4, p2, p3, p4)					
		# This puts the geneID, exonID, FC values, and padjust values 
		# together as one element of a list 
		
		
		# Treatment2 only upregulated exon list:
		if (l2 >= inc and p2 < pv and
			((l3 < inc and l3 > dcr) or p3 > pv) and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment2_only_up.append(val)					# add geneID and exonID to list
			
		# Treatment3 only upregulated exon list:
		if (l3 >= inc and p3 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv) and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment3_only_up.append(val)					# add geneID and exonID to list
		# Treatment4 only upregulated exon list:
		if (l4 >= inc and p4 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv) and
			((l3 < inc and l3 > dcr) or p3 > pv)):
			Treatment4_only_up.append(val)					# add geneID and exonID to list
		# all upregulated exon list:
		if (l2 >= inc and p2 < pv and
			l3 >= inc and p3 < pv and
			l4 >= inc and p4 < pv):
			all_up.append(val)							# add geneID and exonID to list
		# Treatment2 only downregulated exon list:
		if (l2 <= dcr and p2 < pv and
			((l3 < inc and l3 > dcr) or p3 > pv) and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment2_only_down.append(val)					# add geneID and exonID to list
		# Treatment3 only downregulated exon list:
		if (l3 <= dcr and p3 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv) and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment3_only_down.append(val)					# add geneID and exonID to list
		# Treatment4 only downregulated exon list:
		if (l4 <= dcr and p4 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv) and
			((l3 < inc and l3 > dcr) or p3 > pv)):
			Treatment4_only_down.append(val)					# add geneID and exonID to list
		# all downregulated exon list:
		if (l2 <= dcr and p2 < pv and
			l3 <= dcr and p3 < pv and
			l4 <= dcr and p4 < pv):
			all_down.append(val)						# add geneID and exonID to list
		# Treatment2 and Treatment3 only upregulated exon list:
		if (l2 >= inc and p2 < pv and
			l3 >= inc and p3 < pv and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment2_3_up_4_NS.append(val)					# add geneID and exonID to list
		# Treatment2 and Treatment4 only upregulated exon list:
		if (l2 >= inc and p2 < pv and
			l4 >= inc and p4 < pv and
			((l3 < inc and l3 > dcr) or p3 > pv)):
			Treatment2_4_up_3_NS.append(val)					# add geneID and exonID to list
		# Treatment3 and Treatment4 only upregulated exon list:
		if (l3 >= inc and p3 < pv and
			l4 >= inc and p4 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv)):
			Treatment3_4_up_2_NS.append(val)					# add geneID and exonID to list
		# Treatment2 and Treatment3 only downregulated exon list:
		if (l2 <= dcr and p2 < pv and
			l3 <= dcr and p3 < pv and
			((l4 < inc and l4 > dcr) or p4 > pv)):
			Treatment2_3_down_4_NS.append(val)				# add geneID and exonID to list
		# Treatment2 and Treatment4 only downregulated exon list:
		if (l2 <= dcr and p2 < pv and
			l4 <= dcr and p4 < pv and
			((l3 < inc and l3 > dcr) or p3 > pv)):
			Treatment2_4_down_3_NS.append(val)				# add geneID and exonID to list
		# Treatment3 and Treatment4 only downregulated exon list:
		if (l3 <= dcr and p3 < pv and
			l4 <= dcr and p4 < pv and
			((l2 < inc and l2 > dcr) or p2 > pv)):
			Treatment3_4_down_2_NS.append(val)				# add geneID and exonID to list
		# Treatment2 and Treatment3 upregulated and Treatment4 downregulated exon list:
		if (l2 >= inc and p2 < pv and
			l3 >= inc and p3 < pv and
			l4 <= dcr and p4 < pv):
			Treatment2_3_up_4_down.append(val)				# add geneID and exonID to list
		# Treatment2 and Treatment4 upregulated and Treatment3 downregulated exon list:
		if (l2 >= inc and p2 < pv and
			l4 >= inc and p4 < pv and
			l3 <= dcr and p3 < pv):
			Treatment2_4_up_3_down.append(val)				# add geneID and exonID to list
		# Treatment3 and Treatment4 upregulated and Treatment2 downregulated exon list:
		if (l3 >= inc and p3 < pv and
			l4 >= inc and p4 < pv and
			l2 <= dcr and p2 < pv):
			Treatment3_4_up_2_down.append(val)				# add geneID and exonID to list
		# Treatment2 and Treatment3 downregulated and Treatment4 upregulated exon list:
		if (l2 <= dcr and p2 < pv and
			l3 <= dcr and p3 < pv and
			l4 >= inc and p4 < pv):
			Treatment2_3_down_4_up.append(val)				# add geneID and exonID to list
		# Treatment2 and Treatment4 downregulated and Treatment3 upregulated exon list:
		if (l2 <= dcr and p2 < pv and
			l4 <= dcr and p4 < pv and
			l3 >= inc and p3 < pv):
			Treatment2_4_down_3_up.append(val)				# add geneID and exonID to list
		# Treatment3 and Treatment4 downregulated and Treatment2 upregulated exon list:
		if (l3 <= dcr and p3 < pv and
			l4 <= dcr and p4 < pv and
			l2 >= inc and p2 < pv):
			Treatment3_4_down_2_up.append(val)				# add geneID and exonID to list

# Making empty lists for the groups made in the compare_files function:
Treatment2_only_up = []
Treatment3_only_up = []
Treatment4_only_up = []
all_up = []
Treatment2_only_down = []
Treatment3_only_down = []
Treatment4_only_down = []
all_down = []
Treatment2_3_up_4_NS = []
Treatment2_4_up_3_NS = []
Treatment3_4_up_2_NS = []
Treatment2_3_down_4_NS = []
Treatment2_4_down_3_NS = []
Treatment3_4_down_2_NS = []
Treatment2_3_up_4_down = []
Treatment2_4_up_3_down = []
Treatment3_4_up_2_down = []
Treatment2_3_down_4_up = []
Treatment2_4_down_3_up = []
Treatment3_4_down_2_up = []

print "What would you like your adjusted p-value cutoff to be?"

pval_cutoff = float(raw_input('> '))					# converts adjusted p-value
														# cutoff that user inputs into 
														# a number.
print "What would you like your fold change (increase) cutoff to be?"

up_fc_cutoff = float(raw_input('> '))					# converts fold change (increase)
														# cutoff that user inputs into 
														# a number.
down_fc_cutoff = float(1 / up_fc_cutoff)
print "This means your fold change decrease cutoff is %r. Is this correct?" % down_fc_cutoff

response = ""

def check_dFC(r):

	print "Type y for yes and n for no."
	r = raw_input('> ')

	if r == "y":
		print "good"
	elif r == "n":
		print "uh oh"
		print "What is your fold change decrease cutoff?"
		global down_fc_cutoff
		down_fc_cutoff = float(raw_input('> '))
		#print down_fc_cutoff
	else:
		print "invalid response"
		check_dFC(r)

check_dFC(response)

#print down_fc_cutoff

for a in all_files_dict.iterkeys():						# for each dict entry 
														#(going through genes):
														
	compare_files(up_fc_cutoff, down_fc_cutoff, pval_cutoff, a, all_files_dict)					
	# run that geneID entry through compare_files function

# Making a function to print the list made:

def print_comparison (list):							# uses a list fed through.
	for a in list:										# prints each element in the list
		print a

	print "%s exons found" % len(list)					# notes list length
	print "\n"

# Printing each list with print_comparison function and description:
print "Treatment2 only up:"
print_comparison(Treatment2_only_up)
print "Treatment3 only up:"
print_comparison(Treatment3_only_up)
print "Treatment4 only up:"
print_comparison(Treatment4_only_up)
print "All up:"
print_comparison(all_up)
print "Treatment2 only down:"
print_comparison(Treatment2_only_down)
print "Treatment3 only down:"
print_comparison(Treatment3_only_down)
print "Treatment4 only down:"
print_comparison(Treatment4_only_down)
print "All down:"
print_comparison(all_down)
print "Treatment2 and Treatment3 up and Treatment4 not significant:"
print_comparison(Treatment2_3_up_4_NS)
print "Treatment2 and Treatment4 up and Treatment3 not significant:"
print_comparison(Treatment2_4_up_3_NS)
print "Treatment3 and Treatment4 up and Treatment2 not significant:"
print_comparison(Treatment3_4_up_2_NS)
print "Treatment2 and Treatment3 down and Treatment4 not significant:"
print_comparison(Treatment2_3_down_4_NS)
print "Treatment2 and Treatment4 down and Treatment3 not significant:"
print_comparison(Treatment2_4_down_3_NS)
print "Treatment3 and Treatment4 down and Treatment2 not significant:"
print_comparison(Treatment3_4_down_2_NS)
print "Treatment2 and Treatment3 up and Treatment4 down:"
print_comparison(Treatment2_3_up_4_down)
print "Treatment2 and Treatment4 up and Treatment3 down:"
print_comparison(Treatment2_4_up_3_down)
print "Treatment3 and Treatment4 up and Treatment2 down:"
print_comparison(Treatment3_4_up_2_down)
print "Treatment2 and Treatment3 down and Treatment4 up:"
print_comparison(Treatment2_3_down_4_up)
print "Treatment2 and Treatment4 down and Treatment3 up:"
print_comparison(Treatment2_4_down_3_up)
print "Treatment3 and Treatment4 down and Treatment2 up:"
print_comparison(Treatment3_4_down_2_up)