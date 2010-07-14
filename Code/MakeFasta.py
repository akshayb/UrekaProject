from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
import psycopg2
import sys
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Seq import Seq
class DbData:
	def __init__ (self):
		conn = psycopg2.connect ("host='127.0.0.1' dbname='ureka' user='ureka' password='ureka'")
		cursor = conn.cursor()
		query = cursor.execute ("SELECT uniref_id, start, endl, sub_seq FROM id_len")	
		rows = cursor.fetchall()
		conn.commit()
		conn.close()
		self.rows = rows
		

	

if __name__ == '__main__':
	MyData = DbData()
	RecordList = []
	for row in MyData.rows:
		record = SeqRecord(Seq(row[3], IUPAC.protein), id = row[0],name = row[0])
		RecordList.append(record)
		
output_handle = open("meebo.fasta","w")
SeqIO.write(RecordList, output_handle, "fasta")
output_handle.close()


		
		
	
