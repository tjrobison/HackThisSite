wf = open('wordlist.txt', 'r')
words = wf.readlines()
sf = open('scrambled.txt', 'r')
scrambled = sf.readlines()

unscrambled = []

for w1 in scrambled:
	for w2 in words:
		if len(w1) != len(w2):
			pass
		else:
			valid = True
			for l in w1:
				if l not in w1:
					valid = False
					break
			if valid:
				unscrambled.append(w2)
				break

for w in unscrambled:
	print w

