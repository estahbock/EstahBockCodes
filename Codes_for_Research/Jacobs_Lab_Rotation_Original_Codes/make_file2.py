import os,sys,string

# to run this python script type: python make_file.py segway_annotations.txt 

infile = open(sys.argv[1])
file1 = infile.readlines()
infile.close()

output = []

for i in range(len(file1)):

   this_out = "grep -w '%s' k562_segway.bed | wc -l\n"%string.split(string.strip(file1[i]))[0]
   output.append(this_out)
outfile = open('annotations_segway.do','w')
outfile.writelines(output)
outfile.close()

 
