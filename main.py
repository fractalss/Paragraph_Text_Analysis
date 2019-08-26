# Modules
import re
# Reading the input paragraph from the file
para = 'para.txt'
with open(para,'r') as text:
   para_input = text.read()
# Checking for spaces or newline characters or periods or commas to find words
words = re.split('\s|\n|,|\.', para_input)
# Removing null strings from the list of words
words = list(filter(None, words))
# Checking for periods between sentences
sentences = para_input.split(".")
# Last spilt is an empty sentence, therefore decrementing the count by 1
sentences_count = len(sentences)-1
word_count = len(words)
letter_count_per_word = [len(w) for w in words]
letter_count =  sum(letter_count_per_word)
avg_letter_count = letter_count/word_count
avg_sentence_count = word_count/sentences_count

print(" Paragraph Analysis\n")
print("------------------------------\n")
print(f" Approximate Word Count: {word_count}\n")
print(f" Approximate Sentence Count : {sentences_count}\n")
print(f" Average Letter Count : {avg_letter_count}\n")
print(f" Average Sentence Length : {avg_sentence_count}\n")
