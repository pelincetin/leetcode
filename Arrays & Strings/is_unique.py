def is_unique(s):
	a = set()
	is_unique = True
	#assuming 128 character ASCII
	if len(s) > 128:
		return False
	for character in s:
		# sets are implemented as hash tables under the hood
		# o(1) lookup
		if character not in a:
			a.add(character)
		else:
			is_unique = False
	return is_unique

print(is_unique("hello"))

