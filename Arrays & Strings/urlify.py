def urlify_method1(s):
	s = s.replace(" ", "%20")
	return s

def urlify_method2(s):
	result = ''
	for character in s:
		if character == " ":
			result += "%20"
		else:
			result += character
	return result

print(urlify_method1("Mr. John Smith"))
print(urlify_method2("Mr. John Smith"))