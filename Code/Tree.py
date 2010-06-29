import sys
from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped
import psycopg2
import types


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
		IdTempA = sorted(TreeObj.Id)
		for Temp in IdTempA:
			print type(Temp)
			#Feed = (Temp)
			print "1"
			print Temp
			cursor.execute("SELECT seq from uniref102 where uniref_id = %s",(Temp,))

			print "2"
			DataFetch = cursor.fetchone()
			print "Type of output"
			print type(DataFetch)
			if type(DataFetch) is not types.NoneType:
				SeqList.append(cursor.fetchone())
			print "3"
		conn.commit()
		print "Finished gathering all sequeneces from the database"
	except Exception, err:
		sys.stderr.write ('ERROR: %s \n' % str(err))
		conn.rollback()
	STreeId = sorted (TreeObj.Id)
	try:
		for i in range(len(SeqList)):
			Feed = {"Table":"brct_data","Id":STreeId[i],"Seq":SeqList[i]}
			cursor.execute("INSERT INTO %{Table}s (uniref_id,seq) values (%{Id}s, %{Seq})",Feed)
		conn.commit()
	except Exception, err:
		conn.rollback()
		print "Error while inserting into to database"
		sys.stderr.write ('ERROR: %s \n' % str(err))
	
	conn.close()


	
		
		


		 

	

	

