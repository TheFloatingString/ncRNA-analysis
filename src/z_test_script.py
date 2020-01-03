import numpy as np
import json
from statsmodels.stats.weightstats import ztest
from search_motifs import generate_permutations
import pandas as pd
import matplotlib.pyplot as plt

with open("results/ncrna_count-length-8.json", 'r') as jsonfile:
	d = json.load(jsonfile)

with open("results/labels.json", 'r') as jsonfile:
	labels_dict = json.load(jsonfile)

# labels = np.genfromtxt("results/labels.csv")
# print(labels.shape)
# print(type(labels[0]))

cancer_positive_ncrnas = []
cancer_negative_ncrnas = []

for gene_name in list(d.keys()):
	if labels_dict[gene_name] == 0:
		cancer_negative_ncrnas.append(np.array(d[gene_name]))
	elif labels_dict[gene_name] == 1:
		cancer_positive_ncrnas.append(np.array(d[gene_name]))

cancer_positive_ncrnas = np.array(cancer_positive_ncrnas)
cancer_negative_ncrnas = np.array(cancer_negative_ncrnas)

print(cancer_positive_ncrnas.shape)
print(cancer_positive_ncrnas.shape[1])

number_of_features = cancer_positive_ncrnas.shape[1]

# make sure!!!
feature_list = generate_permutations(8)

df_patterns = pd.DataFrame(columns=["pattern", "ztest score"])


for i in range(number_of_features):
	cancer_positive_ncrnas_selection = cancer_positive_ncrnas[:,i]
	cancer_negative_ncrnas_selection = cancer_negative_ncrnas[:,i]
	ztest_score = ztest(cancer_positive_ncrnas_selection, cancer_negative_ncrnas_selection)

	df_patterns.loc[i] = [feature_list[i]] + [ztest_score[0]]
	if i%1000==0:
		print(i)

df_patterns = df_patterns.sort_values(by=["ztest score"], ascending=False)

plt.plot(df_patterns["ztest score"].values)
plt.savefig("results/ztest_distribution-4-solid.png")

print(df_patterns)

df_patterns.to_csv("results/ztest-length-8-solid.csv", index=False)