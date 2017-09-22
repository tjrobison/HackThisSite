import png

KEY = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
'..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
'-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
'.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
'..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
'--.': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
'....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
'----.': '9', '.-.-.-': '.', '--..--': ',', '..--.': '?' }

def count_pixels():
	img_reader = png.Reader(filename='PNG.png')
	image = img_reader.asRGB8()

	pixels = []
	for array in image[2]:
		count = 0
		for p in array:
			if count == 2:
				pixels.append(p)
				count = 0
			else:
				count = count + 1
	index = 0
	pos = [0, 0] 
	morse_raw = []
	for p in pixels:
		if p == 255:
			pos[0] = pos[1]
			pos[1] = index
			morse_raw.append(chr(pos[1] - pos[0]))
		index = index + 1

	morse_letters = []
	letter = ''
	for c in morse_raw:
		if c == ' ':
			morse_letters.append(letter)
			letter = ''
		else:
			letter = letter + c

	final = ''
	for c in morse_letters:
		if c == ' ':
			letter = ' '
		else:
			letter = KEY[c]
		final = final + letter

	return final 
