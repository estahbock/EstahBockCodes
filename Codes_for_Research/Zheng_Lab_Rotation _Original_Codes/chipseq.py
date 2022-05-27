from sys import argv

script, File1, File2 = argv

# converting files into dictionary with following function
def turn_into_dict(file, dict_made):
	file1 = open(file)
	
	for line in file1:
		(key, val1, val2, x) = line.split() # x, here, is something in the file after
		val1 = int(val1)					# what we need. If there are more parts to
		val2 = int(val2)					# each line, will need to modify script
		
		if not dict_made.has_key(key): # checks that is new key
			val_list = [[val1, val2, 0, 0, 0]] # puts placeholder 0's for later assessment
			dict_made[key] = val_list
		else: # if the key has been added, needs to append to list
			val_list.append([val1, val2, 0, 0, 0])
			
	file1.close()

range_parameter = 5000 # can change this number

File1_peaks = {}
turn_into_dict(File1, File1_peaks)
File2_peaks = {}
turn_into_dict(File2, File2_peaks)

############# ONLY USING File1_peaks TO KEEP TRACK
############# (Although shows 3 zeros at end of File2_peaks:
############# artifact of repeating initial function)

# made following function to use for comparison of dictionaries
def compare(chr_, a, b):
	N = len(a[chr_])
	i = 0
	while i < N:
		if b.has_key(chr_):
			M = len(b[chr_])
			j = 0
			while j < M:
				m = a[chr_][i][0]
				n = a[chr_][i][1]
				k = b[chr_][j][0]
				l = b[chr_][j][1]
				if k <= m <= l or k <= n <= l or m <= k <= n or m <= l <= n:
					# checks if either end of a range in b range, 
					# or either end of b range in a range
					# puts 1 in 3rd element because overlaps
					a[chr_][i][2] = 1
				m = a[chr_][i][0] - range_parameter
				n = a[chr_][i][0]
				if k <= m <= l or k <= n <= l or m <= k <= n or m <= l <= n:
					# checks if TF element within range on left side 
					# puts 1 in 4th element because overlaps
					a[chr_][i][3] = 1
				m = a[chr_][i][1]
				n = a[chr_][i][1] + range_parameter
				if k <= m <= l or k <= n <= l or m <= k <= n or m <= l <= n:
					# checks if TF element within range on right side
					# puts 1 in 5th element because overlaps
					a[chr_][i][4] = 1
				j += 1
		print (chr_ + ' ' + str(a[chr_][i][0]) + ' ' + str(a[chr_][i][1]) + ' ' 
			+ str(a[chr_][i][2]) + ' ' + str(a[chr_][i][3]) + ' ' + str(a[chr_][i][4]))
		i += 1

# for loop to apply previous function in a systematic manner
for chr in File1_peaks.iterkeys():
	compare(chr, File1_peaks, File2_peaks)