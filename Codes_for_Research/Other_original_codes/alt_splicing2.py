from sys import argv

script, File1, File2 = argv

# Use metafile_alt_splicing.txt for File1 and Summary_Alt_Splicing.txt for File2
# File1 is a metafile to lead to opening other files to analyze and File2 is a file to
# record all entries of the dictionary made that compiles the data from all files analyzed
Treatment
filelist = open(File1)

# reading file list from metafile:
file_list = []
for line in filelist:
	file_list.append(line.rstrip("\n"))
#print file_list										# command to check script

filelist.close()

# making a function to turn the data into a dictionary
def turn_into_dict(x, dict_made):
	G = len(x)											# G is # of files used.
	i = 0												# counter for file # 
														# (starts with 0 for first)
	while i < G: 										# and stops when out of files.
		
		FILE_X = open(x[i])								# item in file list based
														# on counter
		
		for line in FILE_X:
			if not line.startswith('#'):				# goes through file line by line
			# ignores lines that start with a "#"
				(geneID, exon, log2FC) = line.split()
				# split line into the above variables
				key = "geneID: %s exon: %s" % (geneID, exon)
				# key is both geneID and exon
				log2FC = float(log2FC)					# makes sure log2FC is read as
														# a number to help make 
														# list in dict.
				# if statement to do things differently if key is in dict or key is not
				# in dict and log2FC is < 0 (reflecting downregulation of exon) or
				# log2FC is > 0 (reflecting upregulation of exon):
				# This part is for if key in dict and exon downregulated:
				if log2FC < 0 and key in dict_made:		# if log2FC reflects downregulated
					dict_made[key][i] = -1				# and key in dict, assign -1 to
														# place corresponding to the file
														# being read.
				# This part is for if key not in dict and exon downregulated:
				elif log2FC < 0 and key not in dict_made:
					val_list = []						# val_list is list of log2FC
														# for each comparison
					# k is a counter for the location in val_list the script is at.
					k = 0
					while k < i:						# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(-1)					# puts -1 in correct location.
					k += 1
					while k < G:						# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
						k += 1							# file list.
					dict_made[key] = val_list			# a dict entry is made 
														# with val_list.
				# This part is for if key in dict and exon upregulated:
				elif log2FC > 0 and key in dict_made:	# if log2FC reflects upregulated
					dict_made[key][i] = 1				# and key in dict, assign 1 to
														# place corresponding to the file
														# being read.
				# This part is for if key not in dict and exon upregulated:
				elif log2FC > 0 and key not in dict_made:
					val_list = []
					# k is a counter for the location in val_list the script is at.
					k = 0
					while k < i:						# puts 0 placeholders up until
						val_list.append(0)				# the place in the list of files
						k += 1							# where the script is at.
					val_list.append(1)					# puts 1 in correct location.
					k += 1
					while k < G:						# puts 0 placeholders up until
						val_list.append(0)				# the end of the length of the
						k += 1							# file list.
					dict_made[key] = val_list			# a dict entry is made 
														# with val_list.
					#print key, dict_made[key]			# command to check script
		FILE_X.close()
		i += 1											# moves on to next file

all_files_dict = {}										# makes empty dict.
turn_into_dict(file_list, all_files_dict)				# command to use function that
														# makes dict.
#print all_files_dict									# command to check script

target = open(File2, 'w')								# opens record file (File2), 
														# in writing mode

for a in all_files_dict.iterkeys():						# goes through each key in dict
	print str(a), ' '.join(map(str, all_files_dict[a]))	# and prints entry,
	target.write(str(a))								# writes key to record file,
	target.write(' ')									# puts a space,
	target.write(' '.join(map(str, all_files_dict[a])))	# writes each number in list of
														# entry, with spaces in between,
	target.write("\n")									# and goes to a new line for the
														# next entry.
	
target.close()

# The following code is used to compare the entries from the different files:

# This one prints the geneIDs and exonIDs that go up or down for Treatment2 only:
print "Treatment2 only up or down:"

num1 = 0
# num1 will be used to count the exons found. It starts at 0.
for a in all_files_dict.iterkeys():						# for each dict entry:
	m = all_files_dict[a][0]							# m is the Treatment2 entry for the key
	n = all_files_dict[a][1]							# n is the Treatment3 entry for the key
	o = all_files_dict[a][2]							# o is the Treatment4 entry for the key
	# These variables were used to make the next line shorter
	if m != 0 and n == 0 and o == 0:					# if the Treatment2 value is not 0 and
														# the other values do = 0, 
		print str(a)									# print the geneID and exonID (key)
		num1 += 1										# and count an exon

if num1 == 0:											# if no exons are found (num1 = 0)
	print "no exons found"								# note that
else:
	print "%d exons" % num1								# otherwise, note the # of exons

# This one prints the geneIDs and exonIDs that all go in the same direction:
print "All in same direction:"

num1 = 0
# num1 resets to count the exons found again for this group
for a in all_files_dict.iterkeys():						# for each dict entry:
	m = all_files_dict[a][0]							# variable assignments are
	n = all_files_dict[a][1]							# the same as before
	o = all_files_dict[a][2]
	if m == n == o != 0:								# if all entries are = and
														# not = to 0,
		print str(a)									# print the key
		num1 += 1										# and count an exon

if num1 == 0:											# readout for exon count as before
	print "no exons found"
else:
	print "%d exons" % num1

# This one prints geneIDs and exonIDs for which Treatment2 and Treatment3 go in the same direction
# and Treatment4 goes in the reverse direction
print "Treatment2 and Treatment3 in same direction only and Treatment4 in reverse:"
num1 = 0												# restarts exon count
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]							# same assignments
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if m == n and m != o and m != 0 and o != 0:			# if Treatment2 = Treatment3, Treatment2 is 
														# not = to Treatment4, Treatment2 is
														# not = to 0, and Treatment4 is 
														# not = to 0:
		print str(a)									# print key
		num1 += 1										# count exon #

if num1 == 0:											# readout for exon count
	print "no exons found"
else:
	print "%d exons" % num1

# This one prints geneIDs and exonIDs for which Treatment2 and Treatment3 go in the same direction
# and Treatment4 is not significant
print "Treatment2 and Treatment3 in same direction only and Treatment4 not significant:"
num1 = 0												# restart exon count
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]							# same assignments
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if m == n and m != 0 and o == 0:					# if Treatment2 = Treatment3, Treatment2 is
														# not = to 0, and Treatment3 is 
														# = to 0:
		print str(a)									# print key
		num1 += 1										# count exon #
		
if num1 == 0:											# readout for exon count
	print "no exons found"
else:
	print "%d exons" % num1
########### missing if Treatment2 and 3 in opp directions, etc.
##### Alt better design: use 2d dict and then make lists through 1 for loop and then print the lists with details...
#### That would be much better design. DO THAT!
print "Treatment2 and Treatment4 in same direction only:"
num1 = 0
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if m == o and m != n and m != 0:
		print str(a)
		num1 += 1
if num1 == 0:
	print "no exons found"
else:
	print "%d exons" % num1
	
print "Treatment3 and Treatment4 in same direction only:"
num1 = 0
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if n == o and m != n and n != 0:
		print str(a)
		num1 += 1
if num1 == 0:
	print "no exons found"
else:
	print "%d exons" % num1
	
print "Treatment3 only up or down:"
num1 = 0
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if m == 0 and n != 0 and o == 0:
		print str(a)
		num1 += 1
if num1 == 0:
	print "no exons found"
else:
	print "%d exons" % num1
	
print "Treatment4 only up or down:"
num1 = 0
for a in all_files_dict.iterkeys():
	m = all_files_dict[a][0]
	n = all_files_dict[a][1]
	o = all_files_dict[a][2]
	if m == 0 and n == 0 and o != 0:
		print str(a)
		num1 += 1
if num1 == 0:
	print "no exons found"
else:
	print "%d exons" % num1
