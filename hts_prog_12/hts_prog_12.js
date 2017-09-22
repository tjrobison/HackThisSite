raw=document.getElementsByTagName('input')[0].value;
P = [2,3,5,7];
C = [4,6,8,9];
letters=[];
prime=0;
composite=0;

for (var i = raw.length - 1; i >= 0; i--) {
	number = false;
	for (var i = P.length - 1; i >= 0; i--) {
			if (raw[i] == P[i]) {
				prime += raw[i];
				number = true;
			};	
		};	
	for (var i = C.length - 1; i >= 0; i--) {
			if (raw[i] == C[i]) {
				composite += raw[i];
				number = true;
			};	
		};	
	if (!number && letters.length <= 25) {
		letters.append};
};

product = prime * composite;
final_string = "";
for (var i = letters.length - 1; i >= 0; i--) {
	ascii_code = letters[i].charCodeAt() + 1;
	final_char = String.fromCharCode(ascii_code);
	final_string += final_char;
};
final_string += product;
formInput = document.getElementsByTagName('input')[1];
formSubmit = document.getElementsByTagName('input')[2];
formInput.value = final_string;
