base_pairs = ["A", "C", "G", "T"]

permutations_list = []

# generating permutations
def generate_permutations(layers):
	layers=layers-1
	base_pairs = ["A", "C", "G", "T"]
	permutations_list = base_pairs
	for i in range(layers):
		new_permutations_list = []
		for j in permutations_list:
			for k in base_pairs:
				new_permutations_list.append(j+k)
		permutations_list = new_permutations_list
	return permutations_list

def return_frequency(sample_string, pattern):
	return sample_string.count(pattern)

def return_float_frequency(sample_string, pattern):
	length_sample_string = len(sample_string)
	length_pattern = len(pattern)
	total_score = 0
	start = 0
	end = len(sample_string)
	for i in range(length_sample_string - length_pattern + 1):
		sub_sample_string = sample_string[start: end]
		count_of_matches = 0
		for j in range(length_pattern):
			if sub_sample_string[j] == pattern[j]:
				count_of_matches += 1
		count_of_matches /= length_pattern
		total_score += count_of_matches
		start += 1
		end += 1
	return total_score / (length_sample_string - length_pattern + 1)

def compute_all_frequencies(sample_string, layers, frequency="discrete"):
	overall_list = list()
	if frequency == "discrete":
		for permutation in generate_permutations(layers):
			overall_list.append(return_frequency(sample_string, permutation))
	elif frequency == "continuous":
		for permutation in generate_permutations(layers):
			overall_list.append(return_float_frequency(sample_string, permutation))
	return overall_list

# for rna_sequence in list_of_rna_sequences:
print(return_float_frequency("aaabbbccc", "ax"))