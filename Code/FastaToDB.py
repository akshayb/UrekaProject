from Bio import AlignIO
kdfrom Bio import SeqIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped
import sys
import psycopg

class FileToDb:
	def __init__ (self, FILE, FORMAT,HOST,DB,TABLE,USERNAME,PASSWORD):
		self.FILE = FILE
		self.FORMAT = FORMAT
		self.DATA = AlignIO.read(open(FILE), FORMAT)
		self.HOST = HOST
		self.DB = DB
		self.TABLE = TABLE
		self.USERNAME = USERNAME
		self.PASSWORD = PASSWORD
		self.Id = []
		self.Seq = []
		for Temp in self.DATA:
			self.start
			self.Start.append(Temp.id.split("/")[1].split("-")[0])
			self.End.append(Temp.id.split("/")[1].split("-")[1])

	def insert (self):
		try:
			conn = psycopg.connect ("host="+self.HOST+" dbname="+self.DB+" user="+self.USER)
			print 'Successfully connected to database'
		except:
			print 'Error: Unable to connect to database!'
		
		#create a cursor
		cursor = conn.cursor()
		
		
		try:
			cursor.execute("INSERT INTO uniref100 (uniref_id,seq) values (%{Id}s, %{Seq})",Feed)
		except:
			conn.rollback()



		
	
