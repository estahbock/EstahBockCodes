from sys import argv

script, File1, File2, File3 = argv

# File1 = humansummary, File2 = mousesummary, File3 = complete summary file

def turn_into_dict(x, y, dict_made):
	
	FILE1 = open(x)
	
	for line in FILE1:
		if line.startswith('#'):
			human_genes = line.split()
			human_genes = human_genes[1:]
			n = len(human_genes)
			
	FILE1.close()
	
	FILE2 = open(y)
	for line in FILE2:
		if line.startswith('#'):
			mouse_genes = line.split()
			mouse_genes = mouse_genes[1:]
			m = len(mouse_genes)
			
	FILE2.close()
	
	N = n + m
	
	FILE1 = open(x)
	
	for line in FILE1:
		if not line.startswith('#'):
			x = line.split()
			i = 0
			while i < N - n:
				x.append(0)
				i += 1
			dict_made[x[0]] = x[1:]
			#print x[0], dict_made[x[0]]
	FILE1.close()
	
	FILE2 = open(y)
	for line in FILE2:
		if not line.startswith('#'):
			y = line.split()
			if y[0].upper() not in dict_made and y[0] not in dict_made:
				i = 0
				z = []
				while i < N - m:
					z.append(0)
					i += 1
				i = 1
				while i <= N - n:
					z.append(y[i])
					i += 1
				dict_made[y[0]] = z
				#print y[0], dict_made[y[0]]
			elif y[0] in dict_made:
				dict_made[y[0]][n:N] = y[1:]
				print y[0], dict_made[y[0]]
			else:
				dict_made[y[0].upper()][n:N] = y[1:]
				print y[0].upper(), dict_made[y[0].upper()]
	FILE2.close()

all_files_dict = {}
turn_into_dict(File1, File2, all_files_dict)

FILE1 = open(File1)
for line in FILE1:
	if line.startswith('#'):
		gene_list1 = line.split()
		gene_list1 = gene_list1[1:]
FILE1.close()
FILE2 = open(File2)
for line in FILE2:
	if line.startswith('#'):
		gene_list2 = line.split()
		gene_list2 = gene_list2[1:]
FILE2.close()

#print gene_list1, gene_list2

target = open(File3, 'w')

target.write('#Gene')
target.write(' ')
target.write(' '.join(map(str, gene_list1)))
target.write(' ')
target.write(' '.join(map(str, gene_list2)))
target.write('\n')

for a in all_files_dict.iterkeys():
	#print str(a), ' '.join(map(str, all_files_dict[a]))
	target.write(str(a))
	target.write(' ')
	target.write(' '.join(map(str, all_files_dict[a])))
	target.write("\n")
	
target.close()