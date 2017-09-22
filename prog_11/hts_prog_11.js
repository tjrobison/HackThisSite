x = document.getElementsByTagName('td')[14];
solution = "";

rawShift = x.childNodes[6].textContent;
shift = parseInt(rawShift.split(" ")[1]);

rawAscii = x.childNodes[3].textContent;
codedASCII = rawAscii.split(" ")[2].split("%");
listASCII = codedASCII.slice(0, codedASCII.length-1);
for (var i = listASCII.length - 1; i >= 0; i--) {
	c = parseInt(listASCII[i]) + shift;
	solution = solution + String.fromCharCode(c);	
};
console.log(solution);

formInput = document.getElementsByTagName('input')[0];
formSubmit = document.getElementsByTagName('input')[1];
formInput.value = solution;
formSubmit.click();