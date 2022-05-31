from sys import argv

script, File1 = argv

Data = open(File1)

def dict_for_gene(gene_list, dict_made, a, b):
	for gene in gene_list:
		val_list = []
		N = len(gene_list)
		i = 0
		while i < N:
			val_list.append([a, b])
			i += 1
		dict_made[gene] = val_list

def comp(a, b, dict, i, n):
	k = i + n
	j = i - 1
	l = k - 1
	if int(a[i]) == int(a[k]) and int(a[i]) + int(a[k]) != 0:
		dict[b[j]][l][0] += 1
		dict[b[l]][j][0] += 1
		dict[b[j]][l][1] += 1
		dict[b[l]][j][1] += 1
		#print a
	elif int(a[i]) != int(a[k]) and int(a[i]) + int(a[k]) == 0:
		dict[b[j]][l][1] += 1
		dict[b[l]][j][1] += 1
		#print a

gene_dict = {}
same_in_both = 0
included_in_both = 0

for line in Data:
	if line.startswith('#'):
		row = line.split()
		row = row[1:] #row is list of the genes knocked down/out in order
		#print "Genes", ' '.join(row)
		dict_for_gene(row, gene_dict, same_in_both, included_in_both)
	else:
		next_row = line.split()
		#print next_row
		w = 1
		N = len(row)
		while w < N:
			z = 1
			d = z + w
			while d <= N:
				#print "comp(next_row, row, gene_dict, %r, %r)" %(w, z)
				comp(next_row, row, gene_dict, w, z)
				z += 1
				d = z + w
			if int(next_row[w]) != 0:
				gene_dict[row[w - 1]][w - 1][0] += 1
				gene_dict[row[w - 1]][w - 1][1] += 1
			w += 1
		if int(next_row[w]) != 0:
			gene_dict[row[w - 1]][w - 1][0] += 1
			gene_dict[row[w - 1]][w - 1][1] += 1
		
### make better format for readout...

#print gene_dict

print "Genes", ' '.join(row)

for gene in gene_dict.iterkeys():
	#print str(gene), ' '.join(map(str, gene_dict[gene]))
	print str(gene),
	N = len(row)
	i = 0
	while i < N:
		print "%d/%d" %(gene_dict[gene][i][0], gene_dict[gene][i][1]),
		i += 1
	print "\n"
	print str(gene),
	i = 0
	while i < N:
		if gene_dict[gene][i][1] != 0:
			print float(gene_dict[gene][i][0]) / float(gene_dict[gene][i][1]),
		else:
			print 0,
		i += 1
	print "\n"

Data.close()