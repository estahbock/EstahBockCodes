# This script takes the GI numbers from Scaffold and removes anything before | so it
# can be directly run through the ncbi database:
# http://www.ncbi.nlm.nih.gov/sites/batchentrez
# This script is outdated because a more reliable (and high throughput) matching system 
# is available through other scripts.

# to run this python script type: python gi_only.py gi_list.txt 

# gi_only.py is the script name, python is the language, and gi_list.txt is the  
# txt file made with the gi numbers assigned from Scaffold
# The output is given in terminal, copy and paste to a txt file 
# to download to Batch Entrez

from sys import argv
import re

script, File1 = argv

def command_list(file):
	file1 = open(file)
	
	for line in file1:
		line = line.strip()
		line2 = re.split(r'\|+', line)
		print(line2[1])
		
	file1.close()

command_list(File1)



 
