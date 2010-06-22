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
	LIMIT1 = 450
	LIMIT2 = 2000
	i = 0;
	ScorePoints = []
        for i in xrange(5497):
                ScorePoints.append(0)
	i = 0
	for record in AlignData.Alignment:
	        #print "Here"
		j = 0
		for c in record.seq.tostring():
			if (Score[j] <= LIMIT1):
				if c != '-':
					ScorePoints[i] -= 2
			if (Score[j] >= LIMIT2):
				if c != '-':
					ScorePoints[i] += 2
				else:
					ScorePoints[i] -= 1		
				#NewAlignData.add_sequence(record.seq.tostring(),record.id)
			j += 1
					
		i+=1
#	return NewAlignData
#	return ScorePoints
	i = 0
	DataList = list()
	for record in AlignData.Alignment:
		if(ScorePoints[i] >= 50):
			NewAlignData = Alignment(Gapped(IUPAC.protein,"-"))
			NewAlignData.add_sequence(record.id,record.seq.tostring())
			DataList.append(NewAlignData)
		i+=1

	return ScorePoints

			
				
if __name__ == '__main__':
	AlignData = ReadAlign('new_ncbi.sto','stockholm')
#	AlignData.printAlignment()
	score = getDistributionData (AlignData)
#	print score
#	NewAlignData = formatData(AlignData,score)
	ScorePoints = formatData(AlignData,score)
	print ScorePoints
#	print "Akshay Here"
#	print NewAlignData
#	sum = 0
#	for record in NewAlignData:
#		sum+=1
		#print record
#	print sum
		
#	DataToWrite = WriteAlign(NewAlignData,"new_ncbi.sto","stockholm")
#	DataToWrite.writeToFile()
	
	



