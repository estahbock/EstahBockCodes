from sys import argv

script, File1, File2 = argv

def make_dict(file1, dict_made):
	FILE1 = open(file1)
	for line in FILE1:
		(key, val1) = line.split()
		# turns val1 into a number (that includes decimal)
		val1 = float(val1)
		if val1 < 1:
			dict_made[key] = [val1]
		elif val1 > 1:
			dict_made[key] = [val1]
	FILE1.close()

all_files_dict = {}
make_dict(File1, all_files_dict)

target = open(File2, 'w')
for a in all_files_dict.iterkeys():
	print str(a), ' '.join(map(str, all_files_dict[a]))
	target.write(str(a))
	target.write(' ')
	target.write(' '.join(map(str, all_files_dict[a])))
	target.write("\n")

target.close()