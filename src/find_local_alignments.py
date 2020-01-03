import re

def return_local_align_seq(pattern, sequence_to_search, window_before=40, window_after=40):
	LENGTH_PATTERN = len(pattern)
	list_of_pattern_start_ind = [m.start() for m in re.finditer(f"(?={pattern})", sequence_to_search)]
	list_of_sequences = list()
	for pattern_start_ind in list_of_pattern_start_ind:
		pattern_end_ind = pattern_start_ind + LENGTH_PATTERN
		start_ind = (pattern_start_ind - window_before) if ((pattern_start_ind - window_before) >= 0) else 0
		end_ind = pattern_end_ind + window_after
		list_of_sequences.append(sequence_to_search[start_ind:end_ind])
	return list_of_sequences
