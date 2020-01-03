FILEPATH = "data/GRCh38_latest_rna.fna"
LENGTH_OF_PATTERN = 8

from Bio import SeqIO
import search_motifs
import numpy as np
import json
import time

"""
TODO
* Comment code
* Use Pandas dataframe instead of multiple dicts as JSONs
"""

counter = 4
ids = list()
all_ids = list()

dict_of_ncrna = dict()
dict_of_ncrna_count = dict()


time1 = time.time()

LIST_OF_CANCER = ["MALAT1", "PVT1", "HULC", "HOTAIR", "XIST", "CRNDE", "BANCR", "CCAT2", "LCAL1", "UCA1", "LUADT1", "H19", "NEAT1", "LUADT1", "ZFAS1", "BANCR", "PCA3", "PCAT5", "CASC15", "GAS5"]
labels = list()

for record in SeqIO.parse(FILEPATH, "fasta"):
	if str(record.id)[:2]=="NR":

		ids.append(record.name)
		# print(record)
		record_actual_name = record.description.split('(')[-1].split(')')[0]
		dict_of_ncrna[record_actual_name] = str(record.seq)

time2 = time.time()
print("ELAPSED 1 "+str(round(time2-time1, 3)))


counter = 0
for key_name in dict_of_ncrna.keys():
	result = search_motifs.compute_all_frequencies(dict_of_ncrna[key_name], layers=LENGTH_OF_PATTERN, frequency="discrete")
	dict_of_ncrna_count[key_name] = result
	if counter%10==0:
		print(counter)
	counter += 1

with open(f"results/ncrna_count-length-{str(LENGTH_OF_PATTERN)}.json", 'w') as jsonfile:
	json.dump(dict_of_ncrna_count, jsonfile)

time3 = time.time()
print("ELAPSED 2 "+str(round(time3-time2, 3)))



