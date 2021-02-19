def editInsert(shorter_string, longer_string):
	i, j = 0, 0
	while (i < len(shorter_string) and j < len(longer_string)):
		if (shorter_string[i] != longer_string[j]):
			if (i != j):
				return False
			j += 1
		else:
			i += 1
			j += 1
	return True


def one_away(s1, s2):
	if s1 == s2:
		return True

	# check if their lengths are equal or not
	equal = False
	if len(s1) == len(s2):
		equal = True

	if equal:
		# replacement diff
		one_diff = False
		for i in range(0, len(s1)):
			if s1[i] != s2[i]:
				if one_diff:
					return False
				else:
					one_diff = True
		return True

	else:
		if (abs(len(s1) - len(s2)) != 1):
			return False
		if len(s1) > len(s2):
			return editInsert(s2, s1)
		else:
			return editInsert(s1, s2)

print(one_away("apple", "aple"))
print(one_away("pale", "bale"))
print(one_away("pales", "pale"))
print(one_away("pales", "bale"))