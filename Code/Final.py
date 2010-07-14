import sys
import psycopg2
import types
conn = psycopg2.connect ("host='127.0.0.1' dbname='ureka' user='ureka' password='ureka'")
cursor = conn.cursor()

result1 = cursor.execute("select uniref_id,start,endl,id from id_len")
rows1 = cursor.fetchall()

try:
	for row in rows1:
		print "1"
		print row[0]
		result2 = cursor.execute ("Select seq from id_list where uniref_id = %s",(row[0],))
		print type(result2)
		data = cursor.fetchone()
		print data
		print type(data)
		print type(data[0])
		print "2"
		if type(data[0]) is not types.NoneType:
			seq = data[0]
			start = int(row[1]) - 1 - 10
			print "3"
			end = int(row[2]) -1 + 10
			print "4"
			sbstr = seq[start:end]
			print "5"
			print row[0]
			print row[1]
			print row[2]
			cursor.execute ("Update id_len set sub_seq = %s where id = %s",(sbstr, row[3]))
	conn.commit()
except Exception, err:
	sys.stderr.write ('ERROR : %s .\n' % str(err))
	conn.rollback	
conn.close()

