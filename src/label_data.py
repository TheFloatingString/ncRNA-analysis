FILEPATH = "data/GRCh38_latest_rna.fna"

from Bio import SeqIO
import search_motifs
import numpy as np
import json
import time


LIST_OF_CANCER = ["MALAT1", "PVT1", "HULC", "HOTAIR", "XIST", "CRNDE", "BANCR", "CCAT2", "LCAL1", "UCA1", "LUADT1", "H19", "NEAT1", "LUADT1", "ZFAS1", "BANCR", "PCA3", "PCAT5", "CASC15", "GAS5"]

dict_of_ncrna_labels = dict()

labels = list()

for record in SeqIO.parse(FILEPATH, "fasta"):
	if str(record.id)[:2]=="NR":

		record_actual_name = record.description.split('(')[-1].split(')')[0]
		return_value = 0.0
		if record_actual_name in LIST_OF_CANCER:
			return_value = 1.0

		dict_of_ncrna_labels[record_actual_name] = return_value


with open(f"results/labels.json", 'w') as jsonfile:
	json.dump(dict_of_ncrna_labels, jsonfile)