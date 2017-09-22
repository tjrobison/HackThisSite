def init():
	f = open('encrypted.txt', 'r')
	raw_string = f.readlines()[0][1:]
	raw_num = raw_string.split(' -')
	print raw_num

def eval_cross_total(md5):
	total = 0
	for c in md5:
		total = total + int(c, 16)
	return total

def md5(string):
	m = hashlib.md5()
	m.update(string)
	hashed = m.hexdigest()
	return hashed


def encrypt_string(string, password):
	password_md5 = md5(password)
	md5_total = eval_cross_total(password_md5)
	encrypted_values = []

	for i in xrange(0, len(string)):
		n1 = ord(string[ i:(i+1) ]) 
		n2 = int(password_md5[ (i % 32):(i % 32 + 1) ]) 
		encrypted_values.append(n1 + n2 + md5_total)

		s1 = md5(string[ 0:(i+1) ])[0:16]
		s2 = md5(md5_total)[0:16]
		md5_total = eval_cross_total(s1 + s2)

	implode = ''
	for v in encrypted_values:
		implode.append(v + ' ')

	return implode

