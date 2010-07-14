from Bio import SeqIO
import psycopg2
import sys

conn= psycopg2.connect("host = '127.0.0.1' dbname = 'ureka_home' user= 'ureka' password = 'ureka' ")
cursor = conn.cursor()

handle = open("38AP.fasta","r")
records = list (SeqIO.parse(handle,"fasta"))
for Temp in records:
	print Temp.id
	cursor.execute("UPDATE id_list set seq=%s where uniref_id=%s",(str(Temp.seq),Temp.id))

conn.commit()
conn.close()
	
