#!/usr/bin/python


import snowballstemmer
from termcolor import cprint

words_with_stem = []
words_number = 0
def stem_finder(word):
	st = snowballstemmer.stemmer('english');
	if st.stemWord(word) != word:
		words_with_stem.append(word)	


data_file = open("example.txt","r")

data = data_file.readlines()


for line in data:
		line_list_of_words = line.strip("\n").split(" ")
                for word in line_list_of_words:
					words_number = words_number + 1
					stem_finder(word)

cprint("[+]Total words in file : %s"%words_number,"green")	
cprint("[+]Number of words with stem : %s"%len(words_with_stem),"blue")
#print "[+]List of words : %s"%words_with_stem
