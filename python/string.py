#! /usr/bin/python3
# Filename : string.py

#import re
import string
str1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
str_url = 'pythonchallenge.com/pc/def/map'
#final_url = str_url.maketrans(str_url)
#print(final_url)
final = ''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in str_url:
	if letter in alphabet:
		final += alphabet[(alphabet.index(letter)+2)%26]
#		str2=str1.replace(letter,alphabet[(alphabet.index(letter)+2)%26])
#		str3 = str3.replace(str3[str2.find(letter)],str2[str2.find(letter)])
	else:
		final += letter
print(final)
