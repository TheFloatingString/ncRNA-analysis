FILEPATH = "data/GRCh38_latest_rna.fna"
LENGTH_OF_PATTERN = 8

from Bio import SeqIO
import search_genes
import numpy as np
import json
import time
import pandas as pd

"""
TODO
* Comment code
* Use Pandas dataframe instead of multiple dicts as JSONs
"""

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

df_patterns = pd.DataFrame(columns=["gene", "score"])

counter = 0
for key_name, i in zip(dict_of_ncrna.keys(), range(len(list(dict_of_ncrna.keys())))):
	result = search_genes.search_gene(dict_of_ncrna[key_name])
	# dict_of_ncrna_count[key_name] = result

	df_patterns.loc[i] = [key_name] + [result]

	if counter%1000==0:
		print(counter)
	counter += 1

df_patterns = df_patterns.sort_values(by=["score"], ascending=False)

df_patterns.to_csv("results/genes-scores.csv", index=False)

time3 = time.time()
print("ELAPSED 2 "+str(round(time3-time2, 3)))



