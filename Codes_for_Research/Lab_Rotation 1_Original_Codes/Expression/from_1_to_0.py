# this script converts expression studies with fold change to a format where it is in terms
# of < or > 0
from sys import argv

script, File1, File2 = argv

def make_dict(file1, dict_made):
	FILE1 = open(file1)
	for line in FILE1:
		if not line.startswith('#'):
			(key, val1) = line.split()
			# turns val1 into a number (that includes decimal)
			val1 = float(val1)
			if val1 < 1:
				dict_made[key] = [-1]
			elif val1 > 1:
				dict_made[key] = [1]
	FILE1.close()

all_files_dict = {}
make_dict(File1, all_files_dict)

FILE1 = open(File1)
for line in FILE1:
	if line.startswith('#'):
		header = line.split()
FILE1.close()

target = open(File2, 'w')

target.write(' '.join(map(str, header)))
target.write("\n")

for a in all_files_dict.iterkeys():
	print str(a), ' '.join(map(str, all_files_dict[a]))
	target.write(str(a))
	target.write(' ')
	target.write(' '.join(map(str, all_files_dict[a])))
	target.write("\n")

target.close()