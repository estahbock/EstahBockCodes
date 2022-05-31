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
				# if statement to do different things depending on if key1 (geneID) 
				# and key2 (exon) is in the dict, just key1 is in the dict, or 
				# neither keys are in the dict
				# Structured so there are 3 columns of log2FC, then 3 columns of padjust
				# This part is for if both keys are in the dict:
				if key1 in dict_made and key2 in dict_made[key1]:
					dict_made[key1][key2][i] = log2FC	# puts log2FC in correct location
					j = G + i
					dict_made[key1][key2][j] = padjust	# puts padjust in correct location
					#print key1, key2, dict_made[key1][key2] # command to check script
				# This part is for if key1 (geneID) is in the dict by key2 (exon) is not:
				elif key1 in dict_made and (key2 not in dict_made):
					val_list = []						# val_list is list of log2FC and
														# padjust for each comparison
					# k is a counter for the location in val_list the script is at.
					k = 0
					while k < i:						# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(log2FC)				# puts log2FC in correct location.
					k += 1
					while k < G:						# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
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
					while k < i:						# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(log2FC)				# puts log2FC in correct location
					k += 1
					while k < G:						# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
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