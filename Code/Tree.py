from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped

class Tree:
	def __init__ (self, FILE, FORMAT):
		self.FILE = FILE
		self.FORMAT = FORMAT
		self.DATA = AlignIO.read(open(FILE), FORMAT)
		self.Id = []
		self.Start = []
		self.End = []
		for Temp in self.DATA:
			self.Id.append( Temp.id.split("/")[0])
			self.Start.append(Temp.id.split("/")[1].split("-")[0])
			self.End.append(Temp.id.split("/")[1].split("-")[1])

	def search(self,DB):
		DBFile = open(DB)
		SeqList = list(SeqIO.parse(DBFile,"fasta")
		for i in SeqList:
			
		DBFile.close()
		
		

if __name__ == '__main__':
	TreeObj = Tree("out.fasta","stockholm")
 	for Start in sorted(TreeObj.Id):
		print Start
	print len(TreeObj.Id)	


		 

	

	

