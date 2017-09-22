import os

def create_files():
	"""
	initializes files for visual inspection of data
	"""
	if os.path.exists('outfile.txt'):
		os.remove('outfile.txt')
	outfile = open('outfile.txt', 'w')
	if os.path.exists('count_dict.txt'):
		os.remove('count_dict.txt')
	cd_file = open('count_dict.txt', 'w')

def read_data():
	f = open('real6test.txt', 'r')
	data = f.readlines()
	return data

def clean_raw(data):
	"""
	cleans up raw encryption and returns
	concatinated list with . removed
	"""
	r1 = []
	for l in data:
		r1.append(l[:-2])
	s1 = ''
	for l in r1:
		s1 = s1 + l
	s1 = s1[1:] + '70'

	try:
		r2 = s1.split('.')
		print len(r2) / 3
	except len(r2)%3 != 0:
		print "Something is wrong with your parsing motherfucker"

	return r2

def sum_vals(data):
	"""
	returns list containing summed triplets
	"""
	summed_vals = []
	summation = 0
	temp_vals = ''
	count = -1
	min_val = 9999
	max_val = 0
	for l in data:
		if count == 2:
			print temp_vals + '= ' + str(summation)
			summed_vals.append(summation)
			#outfile.write(str(summation) + '\n')
			count = 0
			summation = int(l)
			temp_vals = l + ' '
		else:
			temp_vals = temp_vals + l + ' '
			summation = summation + int(l)
			count = count + 1
	return summed_vals 

def count_reps(data):
	"""
	returns a dict with the occurances of
	individual summed values
	"""
	count_dict = {}
	for n in data:
		if not count_dict.has_key(n):
			count_dict[n] = 1
		else:
			count_dict[n] = count_dict[n] + 1

	for k in count_dict:
		s = str(k) + ' : ' + str(count_dict[k])
		#cd_file.write(s + '\n')

	return count_dict

def sort_dict(count_dict):
	d = {}
	for v in count_dict.values():
		if v not in d.keys():
			d[v] = '' 

	for n in count_dict:
		k = count_dict[n]
		d[k] = d[k] + ', ' + str(n)
	return d

def create_draft(summed):
	draft = []
	for n in summed:
		if n == 794

def print_final(num_list):
	final = ''
	for n in num_list:
		if type(n) == int:
			final = final + '_'
		else:
			final = final + n
	print final
	return final

def main():
	clean_raw()