#Project Euler
#Problem 17: Number letter counts
#Description: If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#			  If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

ones = {1 : "one",
		2 : "two",
		3 : "three",
		4 : "four",
		5 : "five",
		6 : "six",
		7 : "seven",
		8 : "eight",
		9 : "nine",
		10 : "ten",
		11 : "eleven",
		12 : "twelve",
		13 : "thirteen",
		14 : "fourteen",
		15 : "fifteen",
		16 : "sixteen",
		17 : "seventeen",
		18 : "eighteem",
		19 : "nineteen"}

tens = {2 : "twenty",
		3 : "thirty",
		4 : "forty",
		5 : "fifty",
		6 : "sixty",
		7 : "seventy",
		8 : "eighty",
		9 : "ninety"}

def number_to_letters(n):
	number = str(n)
	# if(len(number) == 1):
	# 	return ones[n]
	string = ""
	if(len(number) <= 2):
		if(n in ones):
			return ones[n]
		if(number[1] == "0"):
			return tens[int(number[0])]			
		else:
			string = tens[int(number[0])] + ones[int(number[1])]
			return string

	if(len(number) == 3):
		if(number[1:] == "00"):
			return ones[int(number[0])] + "hundred"
		if(int(number[1:]) in ones):
			return ones[int(number[0])] + "hundredand" + ones[int(number[1:])]
		if(number[1] == "0"):
			return ones[int(number[0])] + "hundredand" + ones[int(number[2])]
		if(number[2] == "0"):
			return ones[int(number[0])] + "hundredand" + tens[int(number[1])]
		string = ones[int(number[0])] + "hundredand"
		if(int(number[1:]) in ones):
			string += number[int(number[1:])]
		if(number[1] == 0):
			string += tens[int(number[1])]	
		else:
			string += tens[int(number[1])] + ones[int(number[2])]
		return string

	if(len(number) == 4):
		return "onethousand"		


total = 0
for i in range(1, 1001):
	total += len(number_to_letters(i))

print total






