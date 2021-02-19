# i will assume that this problem is case-sensitive
# and whitespace is significant

def is_permutation_method1(s1, s2):
	#because I am using sorted(), the big O is nlogn
	if (len(s1) != len(s2)):
		return False
	s1 = sorted(s1)
	s2 = sorted(s2)
	for i in range(0, len(s1)):
		if s1[i] != s2[i]:
			return False
	return True

def is_permutation_method2(s1, s2):
	# big o is o(n)
	if (len(s1) != len(s2)):
		return False
	lookup_s1 = dict()
	lookup_s2 = dict()
	#{"d": 1, "o": 1, "g": 1}
	for i in s1:
		if i in lookup_s1:
			lookup_s1[i] = lookup_s1.get(i) + 1
		else:
			lookup_s1[i] = 1
	#{"G": 1, "o": 1, "d": 1}		
	for i in s2:
		if i in lookup_s2:
			lookup_s2[i] = lookup_s2.get(i) + 1
		else:
			lookup_s2[i] = 1

	# lookup_s1 = {"d": 1, "o": 1, "g": 1}
	# lookup_s2 = {"G": 1, "o": 1, "d": 1}	
	for i in lookup_s1.keys():
		if i not in lookup_s2:
			return False
		elif lookup_s1.get(i) != lookup_s2.get(i):
			return False
	return True
	print(lookup_s1)


print(is_permutation_method1("dog", "god"))
print(is_permutation_method2("dog", "God"))
