import sys

File = open("try.fasta","r")
for i in File:
	if i[0] == '>':
		print 1
	else:
		print 0

