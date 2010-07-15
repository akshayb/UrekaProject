from Bio import AlignIO
from Bio.Align.Generic import Alignment
from Bio.Alphabet import IUPAC, Gapped

Alignment = AlignIO.read(open("new_meebo.sto","r"), "stockholm")
#AlignIO.write(Alignment, open("new_meebo.fasta","w"), "fasta")
RecordList = []
for record in Alignment:
	new_record = SeqRecord(Seq(str(record.seq), IUPAC.protein), id = record.id, name = record.id)
	RecordList.append(record)

output_handle  = open("new_meebo.fasta","w")
SeqIO.write(RecordList, output_handle, "fasta")
output.handle.close()


