import json
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

from operator import itemgetter

with open("results/ncrna_count-length-4.json", 'r') as jsonfile:
	ncrna_dict = json.load(jsonfile)

with open("results/labels.json", 'r') as jsonfile:
	labels_dict = json.load(jsonfile)

labels = list()
master_dataset = list()

for gene_name in list(ncrna_dict.keys()):

	array = np.array(ncrna_dict[gene_name])
	specified_indices = np.take(array, [127,187,251,238,190,249,95,254,124,92,239,253,159])

	master_dataset.append(specified_indices)
	labels.append([labels_dict[gene_name]])

master_dataset = np.array(master_dataset)
print(master_dataset.shape)
print(np.array(labels).shape)

model = Sequential()
model.add(Dense(12, input_dim=13, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'mse'])
# fit the keras model on the dataset
model.fit(master_dataset, np.array(labels), epochs=2, batch_size=1000, verbose=2)

predictions = model.predict(master_dataset)
predictions_final = list(zip(list(labels_dict.keys()), predictions))
predictions_final = sorted(predictions_final, key=itemgetter(1), reverse=True)

final_array = []

for row in predictions_final:
	temp_row = []
	print(row[0], end='\t')
	print(row[1][0])
	temp_row=[row[0], row[1][0]]
	final_array.append(temp_row)

final_array = np.array(final_array)
# print(predictions_final)

np.savetxt("results/ranked_genes.csv", final_array, fmt="%s")