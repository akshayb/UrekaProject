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
	DB = 'ureka_home'
	USERNAME = 'ureka'
	PASSWORD = 'ureka'
	conn = psycopg2.connect ("host='"+HOST+"' dbname='"+DB+"' user='"+USERNAME + "'password = '" + PASSWORD +"'")
	cursor = conn.cursor()
	print "connection and cursor made"
	try:
		print "Entering the try and catch statement and going to select all the sequences with the target id in the already selected sequences"
		IdTempA = len(TreeObj.Id)
		for Temp in range(IdTempA):
			print type(Temp)
			#Feed = (Temp)
			print "1"
			print Temp
			cursor.execute("INSERT INTO id_len (uniref_id,start,endl) values (%s, %s, %s)",(TreeObj.Id[Temp],TreeObj.Start[Temp], TreeObj.End[Temp]))

			print "2"
		conn.commit()

		print "Finished gathering all sequeneces from the database"
	except Exception, err:
		sys.stderr.write ('ERROR: %s \n' % str(err))
		conn.rollback()
	
	conn.close()


