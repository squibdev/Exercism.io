import string

def is_pangram(sentence):
    for letter in string.ascii_lowercase:
    	if letter in sentence.lower():
    		pass
    	else:
    		return False
    return True