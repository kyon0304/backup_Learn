#! /usr/bin/python3
# Filename: pychlng.py

import re
fakeword=re.compile('(?:[a-z]{1}[A-Z]{3}){2}[a-z]')
file_object=open("re.txt",'r');
text=''
try:
	for letter in file_object:
		text += letter
	re_fake=fakeword.findall(text)
	if re_fake != None:
		for re_word in re_fake:
			print(re_word)
	else:
		print('None')
finally:
	file_object.close()
