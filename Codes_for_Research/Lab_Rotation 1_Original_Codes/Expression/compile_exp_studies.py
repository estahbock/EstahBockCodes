# This script compares expression studies in mice or humans
from sys import argv

script, File1, File2 = argv

filelist = open(File1)

file_list = []
for line in filelist:
	file_list.append(line.rstrip("\n"))
#print file_list

filelist.close()

# File1 = metafile, File2 = output file

def turn_into_dict(x, dict_made):
	G = len(x) ## need extra 0's at end for if missing in later files
	i = 0
	while i < G:
		FILE_X = open(x[i])
	# assumes format where says NA if not significant, has a number < 0 if downregulated,
	# or has a number > 0 if upregulated:
		for line in FILE_X:
			if not line.startswith('#'):
				(key, val1) = line.split()
		# avoiding error from NA and turns val1 into a number (that includes decimal)
				if val1 == 'NA':
					val1 = 0
				else:
					val1 = float(val1)
				if val1 < 0 and key in dict_made:
					dict_made[key][i] = -1
				elif val1 < 0 and key not in dict_made:
					val_list = []
					k = 0
					while k < i:
						val_list.append(0)
						k += 1
					val_list.append(-1)
					k += 1
					while k < G:
						val_list.append(0)
						k += 1
					dict_made[key] = val_list
				elif val1 > 0 and key in dict_made:
					dict_made[key][i] = 1
				elif val1 > 0 and key not in dict_made:
					val_list = []
					k = 0
					while k < i:
						val_list.append(0)
						k += 1
					val_list.append(1)
					k += 1
					while k < G:
						val_list.append(0)
						k += 1
					dict_made[key] = val_list
					#print key, dict_made[key]
		FILE_X.close()
		i += 1

all_files_dict = {}
turn_into_dict(file_list, all_files_dict)
#print all_files_dict

target = open(File2, 'w')

new_file_list = []
for i in file_list:
	i = i[:-1][:-1][:-1][:-1]
	new_file_list.append(i)
print new_file_list

target.write('#Gene')
target.write(' ')
target.write(' '.join(map(str, new_file_list)))
target.write('\n')

for a in all_files_dict.iterkeys():
	print str(a), ' '.join(map(str, all_files_dict[a]))
	target.write(str(a))
	target.write(' ')
	target.write(' '.join(map(str, all_files_dict[a])))
	target.write("\n")
	
target.close()
	
#Just printed gene followed by if upregulated (1), downregulated (-1), 
# or the same/unknown (0) for each of the KO/KD studies 
# with excel (turned to txt) files
