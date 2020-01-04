import re

def search_gene(input_sequence, consider_length=False):
	score = 0.0
	SEQUENCE_LENGTH = len(input_sequence)

	# looking at CCATCG
	pos = [m.start() for m in re.finditer(f"(?=CCATCG)", input_sequence)]
	if consider_length:
		score += len(pos)/SEQUENCE_LENGTH
	else:
		score += 1 if len(pos)>0 else 0

	if consider_length:
		if len(pos) > 0:
			for position in pos:
				if "CTTTT" in input_sequence[position+8:position+48]:
					score += 1/SEQUENCE_LENGTH

	else:
		if len(pos) > 0:
			for position in pos:
				if "CTTTT" in input_sequence[position+8:position+48]:
					score += 1
					break

	# looking at CCATGCAC
	pos = [m.start() for m in re.finditer(f"(?=CCATGCAC)", input_sequence)]
	if consider_length:
		score += len(pos)/SEQUENCE_LENGTH
	else:
		score += 1 if len(pos)>0 else 0

	if consider_length:
		if len(pos) > 0:
			for position in pos:
				if "TCATC" in input_sequence[position+8:position+48]:
					score += 1/SEQUENCE_LENGTH

	else:
		if len(pos) > 0:
			for position in pos:
				if "TCATC" in input_sequence[position+8:position+48]:
					score += 1
					break

	# looking at CTCTCTTT
	COEFF=4
	pos = [m.start() for m in re.finditer(f"(?=CTCTCTTT)", input_sequence)]
	# score += len(pos)*COEFF
	if consider_length:
		score += len(pos)/SEQUENCE_LENGTH
	else:
		score += 1 if len(pos)>0 else 0

	return score