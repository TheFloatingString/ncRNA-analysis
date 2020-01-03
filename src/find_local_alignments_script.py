FILEPATH = "data/GRCh38_latest_rna.fna"
LENGTH_OF_PATTERN = 8

from Bio import SeqIO
import find_local_alignments
import numpy as np
import json
import time
import csv


ids = list()
all_ids = list()

dict_of_ncrna = dict()
ncrna_motifs = list()

time1 = time.time()

LIST_OF_CANCER = ["MALAT1", "PVT1", "HULC", "HOTAIR", "XIST", "CRNDE", "BANCR", "CCAT2", "LCAL1", "UCA1", "LUADT1", "H19", "NEAT1", "LUADT1", "ZFAS1", "BANCR", "PCA3", "PCAT5", "CASC15", "GAS5"]
labels = list()

for record in SeqIO.parse(FILEPATH, "fasta"):
	if str(record.id)[:2]=="NR":

		ids.append(record.name)

		record_actual_name = record.description.split('(')[-1].split(')')[0]
		dict_of_ncrna[record_actual_name] = str(record.seq)

time2 = time.time()
print("ELAPSED 1 "+str(round(time2-time1, 3)))


counter = 0
for key_name in dict_of_ncrna.keys():
	results = find_local_alignments.return_local_align_seq("CCATGCAC", dict_of_ncrna[key_name])
	temp_lists = list()
	for i in results:
		ncrna_motifs.append([i, key_name])
	if counter%100==0:
		print(counter)
	counter += 1

with open(f"results/alignment-CCATGCAC.csv", 'w', newline='\n') as csvfile:
	writer = csv.writer(csvfile, delimiter='\t')
	writer.writerows(ncrna_motifs)

time3 = time.time()
print("ELAPSED 2 "+str(round(time3-time2, 3)))



