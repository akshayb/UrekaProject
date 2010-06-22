import sys
from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped
import psycopg2


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

		

if __name__ == '__main__':
	print "Inside Mai"
	TreeObj = Tree("out.fasta","stockholm")
# 	for Start in sorted(TreeObj.Id):
#		print Start
#	print len(TreeObj.Id)	
	SeqList = []
	print "Going to make connections"
	HOST = '127.0.0.1'
	DB = 'ureka'
	USERNAME = 'ureka'
	PASSWORD = 'ureka'
	conn = psycopg2.connect ("host='"+HOST+"' dbname='"+DB+"' user='"+USERNAME + "'password = '" + PASSWORD +"'")
	cursor = conn.cursor()
	print "connection and cursor made"
	try:
		print "Entering the try and catch statement and going to select all the sequences with the target id in the already selected sequences"
		for Temp in sorted(TreeObj.Id):
			print type(Temp)
			#Feed = (Temp)
			print "1"
			cursor.execute("SELECT seq from uniref101 where uniref_id = %s",(Temp,))
			print "2"
			DataFetch = cursor.fetchone()
			if DataFetch !=  'None':
				SeqList.append(cursor.fetchone())
			print "3"
		conn.commit()
		print "Finished gathering all sequeneces from the database"
	except Exception, err:
		sys.stderr.write ('ERROR: %s \n' % str(err))
		conn.rollback()
	
	conn.close()
	for Temp in SeqList:
		print Temp

	
	
		
		


		 

	

	

