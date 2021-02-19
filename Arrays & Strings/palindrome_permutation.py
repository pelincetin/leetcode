def palindrome_permutation(s):
	# to be a palindrome permutation, each char has to appear twice
	# except for one char, the middle char can appear once if 
	# the length is odd

	# i assume this problem is not case sensitive

	# we don't care about whitespace
	s = s.replace(" ", "")

	# set a boolean flag for odd length
	if len(s) % 2 == 1:
		odd = True
		mid_char_found = False
	else:
		odd = False

	char_lookup = dict()
	for character in s:
		character = character.lower()
		if character in char_lookup:
			char_lookup[character] = char_lookup.get(character) + 1
		else:
			char_lookup[character] = 1
	print(char_lookup)
	
	if odd:
		for character in char_lookup.keys():
			if (char_lookup.get(character) % 2 != 0) and (mid_char_found == False):
				mid_char_found = True
			elif (char_lookup.get(character) % 2 != 0) and (mid_char_found == True):
				return False
		return True

	else:
		for character in char_lookup.keys():
			if char_lookup.get(character) % 2 != 0:
				return False
		return True
	

print(palindrome_permutation("d ogg d"))
print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("Tact Coaa"))
print(palindrome_permutation("hello"))
print(palindrome_permutation("hellla"))
print(palindrome_permutation("pele"))

