import json
import numpy as np
from search_motifs import generate_permutations
import time
import csv

start = time.time()

with open("results/ncrna-onconc-count-length-8.json", 'r') as jsonfile:
	d = json.load(jsonfile)

cancer_positive_ncrnas = list()

for gene_name in list(d.keys()):
	cancer_positive_ncrnas.append(np.array(d[gene_name]))

print(f"ELAPSED {time.time() - start}")

cancer_positive_ncrnas = np.array(cancer_positive_ncrnas)

number_of_features = cancer_positive_ncrnas.shape[1]

feature_list = generate_permutations(8)

final_array = []

print(cancer_positive_ncrnas.shape)

for i in range(number_of_features):
	vertical_slice = cancer_positive_ncrnas[:,i]
	if [x>0 for x in vertical_slice].count(True)>3:
		final_array.append([feature_list[i], vertical_slice, [x>0 for x in vertical_slice].count(True)])
		print("True")
print(f"ELAPSED {time.time() - start}")


with open(f"results/onconc-motifs.csv", 'w', newline='\n') as csvfile:
	writer = csv.writer(csvfile, delimiter='\t')
	writer.writerows(final_array)
print(f"ELAPSED {time.time() - start}")
