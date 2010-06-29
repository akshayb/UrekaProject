from Bio import AlignIO
from Bio import SeqIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped
import sys
import psycopg2

class FileToDb:
	def __init__ (self, FILE, FORMAT,HOST,DB,TABLE,USERNAME,PASSWORD):
		self.FILE = FILE
		self.FORMAT = FORMAT
#		self.DATA = AlignIO.read(open(FILE), FORMAT)
		self.DATA = open(FILE)
		self.HOST = HOST
		self.DB = DB
		self.TABLE = TABLE
		self.USERNAME = USERNAME
		self.PASSWORD = PASSWORD
		self.Id = []
		self.Seq = []
#		for Temp in self.DATA:
#			self.start
#			self.Start.append(Temp.id.split("/")[1].split("-")[0])
#			self.End.append(Temp.id.split("/")[1].split("-")[1])

	def insert (self):
		DbState = 0
		DataState = 1
		#try:
		conn = psycopg2.connect ("host='"+self.HOST+"' dbname='"+self.DB+"' user='"+self.USERNAME + "'password = '" + self.PASSWORD +"'")
		print 'Successfully connected to database'
		#except:
		#	print 'Error: Unable to connect to database!'
		
		#create a cursor
		cursor = conn.cursor()
		PrevUnirefId = 0
		UnirefId = 0
		Seq = 0
		DataState = 0
		DbState = 1
		print "Going in LOOP"	
		for Temp in self.DATA:
			if Temp[0] == '>':
				print "In true >"
				DataState += 1;
				PrevUnirefId = UnirefId
				PrevSeq = Seq
				UnirefId = Temp.split('>')[1].split(' ')[0]
				Seq = ''
			else:
				print "In false >"
				Seq += Temp
			if (DataState> DbState):
				try:
					print "Going to insert entry"
					Feed = (PrevUnirefId, PrevSeq)
					cursor.execute("INSERT INTO uniref102 (uniref_id,seq) values (%s, %s)",Feed)
					print DataState
					print DbState
					DbState += 1
				except Exception, err:
					sys.stderr.write ('ERROR: %s\n' % str(err))
					conn.rollback()

			
		conn.commit()
		conn.close()


if __name__ == '__main__':
	Obj =  FileToDb('uniref100.fasta','fasta','127.0.0.1','ureka','uniref101','ureka','ureka')
	Obj.insert()


		
	
