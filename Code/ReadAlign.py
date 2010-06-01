from Bio import AlignIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped

class ReadAlign:
	def __init__ (self, FILE, FORMAT):
		self.FILE = FILE
		self.FORMAT = FORMAT
		self.Alignment = AlignIO.read(open(FILE),FORMAT)
		
	def printAlignment (self):
		for Record in self.Alignment:
			print Record.seq, Record.id, len(Record.seq)

	def returnAlignment (self):
		return self.Alignment

class WriteAlign:
	def __init__ (self, AlignData, FILE, FORMAT ):
		self.FILE = FILE
		self.FORMAT = FORMAT
		self.Alignment = AlignData
		
	def writeToFile (self):
		AlignIO.write(self.Alignment,open(self.FILE,"w"),self.FORMAT);


def getDistributionData (AlignData):
	score = []
	for i in xrange(485):
		score.append(0)
	for record in AlignData.Alignment:
		i = 0
		for c in record.seq:
			if (c != '-'):
				score[i] += 1
			i+=1
	return (score)

def formatData (AlignData, Score):
	LIMIT = 1000
	i = 0;
	NewAlignData = Alignment(Gapped(IUPAC.protein,"-"))
	for record in AlignData.Alignment:
	        print "Here"
		if (Score[i] >= LIMIT):
			print type(record.seq)
			print type(record.id)
			NewAlignData.add_sequence(record.seq.tostring(),record.id)
		i+=1
	return NewAlignData
				
if __name__ == '__main__':
	AlignData = ReadAlign('ncbi.sto','stockholm')
#	AlignData.printAlignment()
	score = getDistributionData (AlignData)
#	print score
	NewAlignData = formatData(AlignData,score)
	print "Akshay Here"
	print NewAlignData
	DataToWrite = WriteAlign(NewAlignData,"new_ncbi.sto","stockholm")
	DataToWrite.writeToFile()
	
	



