#!/usr/bin/python


import snowballstemmer #import snowballstemmer library
from termcolor import cprint #import cprint method from termcolor library to print colored strings

words_with_stem = [] #list to save all words founded with stem
words_number = 0 #counter to count all word numbers
def stem_finder(word): # function to find the stem using snowballstemmer
	st = snowballstemmer.stemmer('english'); #choose english language stemmer
	if st.stemWord(word) != word: #if the word changed that means a stem was found
		words_with_stem.append(word) #append word to words_with_stem list 


data_file = open("example.txt","r") #open out example text file

data = data_file.readlines() #read lines from the file


for line in data: #split lines from the data variable
		line_list_of_words = line.strip("\n").split(" ") # split the line to words
                for word in line_list_of_words: #check every word in the line 
					words_number = words_number + 1 # add one to the counter 
					stem_finder(word) #check for stem

cprint("[+]Total words in file : %s"%words_number,"green")  #print the words_number variable
cprint("[+]Number of words with stem : %s"%len(words_with_stem),"blue") #print the length of words_with_stem list
#print "[+]List of words : %s"%words_with_stem #uncomment this line to print all words_with_stem list
