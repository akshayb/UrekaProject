import sys
from Bio import AlignIO
from Bio import SeqIO
import psycopg2

FILE = "out.fasta"
FORMAT = "stockholm"
DATA = AlignIO.read(open(FILE), FORMAT)
Id = []
Start = []
End = []
for Temp in DATA:
       Id.append( Temp.id.split("/")[0])
       Start.append(Temp.id.split("/")[1].split("-")[0])
       End.append(Temp.id.split("/")[1].split("-")[1])
print len(Id)

conn = psycopg2.connect("host='127.0.0.1' dbname='ureka_home' user='ureka' password='ureka' ")
cursor = conn.cursor()

try:
	for Temp in Id:
		cursor.execute ("INSERT INTO id_list (uniref_id) values (%s)",(Temp,))
except Exception, err:
	sys.stderr.write ('ERROR : %s \n' %  str(err))
	conn.rollback()

conn.commit()
conn.close()
	
