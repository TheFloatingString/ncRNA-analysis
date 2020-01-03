import json
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

with open("results/ncrna_count-length-continuous-4.json", 'r') as jsonfile:
	d = json.load(jsonfile)

print("Done!")

array_of_values = []

for key in list(d.keys()):
	array_of_values.append(d[key])

pca = PCA(n_components = 256)
pca.fit(array_of_values)
fitted_values = pca.transform(array_of_values)

list_of_genes = ["MALAT1", "PVT1", "HULC", "HOTAIR", "XIST", "CRNDE", "BANCR", "CCAT2", "LCAL1", "UCA1", "LUADT1", "H19", "NEAT1", "LUADT1", "ZFAS1", "BANCR", "PCA3", "PCAT5", "CASC15", "GAS5"]
list_of_gene_sequences = [d[gene_name] for gene_name in list_of_genes]


specific_value = np.array(pca.transform(list_of_gene_sequences))


print(fitted_values.shape)
plt.scatter(fitted_values[:, 0], fitted_values[:, 1], s=.001, alpha=.1, c="blue")
plt.scatter(specific_value[:, 0], specific_value[:, 1], s=0.005, alpha=1, c="red")
# plt.xlim(-200,200)
# plt.ylim(-200,200)
plt.savefig("results/img/ncrna_pca-continuous.jpg", dpi=500)

