


import sys

#read the input and output filename from the command line
#make sure you get these the right way round, or the script will
#DELETE the input file!!
inputfile = sys.argv[1]

#open both files
f = open(inputfile)


for line in f:
    cols = line.strip().split("\t")
    print cols[0] + "\t" +  cols[3] + "\t" +  cols[4]

exit
			




