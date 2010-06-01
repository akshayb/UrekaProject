"""
Module Description:
This file imports PDB files from Network, and store them at appropiate place
"""

from Bio.PDB import PDBList

PDBListTemp = PDBList()
FILE = open("pfam_list.txt","r")
IN = FILE.readline()
while IN:
	print IN
	PDBListTemp.retrieve_pdb_file(IN)
	
	



