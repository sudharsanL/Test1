#Find duplicates in a string

sentence = "Hello hi hello hi Hello hi"
sentence_splitted = sentence.split()
words_list = list(sentence_splitted)
unique_words_list = []
duplicates_words_list = []
duplicates_index = {}

#find duplicates

for word in words_list:
    if word not in unique_words_list:
        unique_words_list.append(word)
    else:
        duplicates_words_list.append(word)

#print the index of the duplicate words:
for dup_word in duplicates_words_list:
    if dup_word in words_list:
        duplicates_index[dup_word] = words_list.index(dup_word)
        # duplicates_index.update({dup_word : words_list.index(dup_word)})

print(f"Duplicate words: {duplicates_words_list}")
print(f"duplicate words index: {duplicates_index}")
        
# print(f"Unique words: {unique_words_list}")
# print(f"Duplicate words: {duplicates_words_list}")



