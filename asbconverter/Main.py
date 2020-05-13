#!/home/username/Desktop python3
# import do argv para receber os parametro passados numa lista com o nome argv
import sys
from sys import argv
import top, end, seqname


# This will open the the file passed in the parameter with index 1
fasta_file = open('example.fasta', 'r')


# This will give the result of the function contain on the modules, to soon be used
dict1 = seqname.fileparser(fasta_file)
beginNexus = top.top(dict1)
endNexus = end.end()

# This for loop has the goal of add spaces of a nexus file
DNA = ""
for i, j in dict1.items():
    DNA += "\t" + i + "  " + j + "\n"


# We redirected the nexus conversion to the standard output
print(beginNexus)
print(DNA)
print(endNexus)


