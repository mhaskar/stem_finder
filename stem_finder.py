#!/usr/bin/python


import snowballstemmer

words_with_stem = []

def stem_finder(word):
	st = snowballstemmer.stemmer('english');
	if st.stemWord(word) != word:
		words_with_stem.append(word)	


data_file = open("example.txt","r")

data = data_file.readlines()

for line in data:
		line_list_of_words = line.strip("\n").split(" ")
		for word in line_list_of_words:
			stem_finder(word)
		
print "[+]Words with stem found : %s"%len(words_with_stem)		
print "[+]List of words : %s"%words_with_stem
