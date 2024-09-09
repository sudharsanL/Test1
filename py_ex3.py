#Find duplicates in a string

sentence = "hello Hello hi hello hi Hello hi Hello"
sentence_splitted = sentence.split()
words_list = list(sentence_splitted)
unique_words_list = []
duplicates_words_set = set()
duplicates_index = {}

#find duplicates
i = 0
while(i<len(words_list)):
    if words_list[i] not in unique_words_list:
        unique_words_list.append(words_list[i])
    else:
        duplicates_words_set.add(words_list[i])
    i+=1

#print the index of the duplicate words:
duplicates_words_list = list(duplicates_words_set)
j=0
while(j<len(duplicates_words_list)):
    if duplicates_words_list[j] in words_list:
        duplicates_index[duplicates_words_list[j]] = words_list.index(duplicates_words_list[j])
        # duplicates_index.update({dup_word : words_list.index(dup_word)})
    j+=1

print(f"Duplicate words: {duplicates_words_set}")
print(f"duplicate words index: {duplicates_index}")
        
# print(f"Unique words: {unique_words_list}")
# print(f"Duplicate words: {duplicates_words_set}")