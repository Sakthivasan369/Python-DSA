input_Sequence=input("Enter a comma-separated sequence of words ")
words_list=[word.strip()for word in input_Sequence.split(",")]
unique_words=sorted(set(words_list))
print("Unique words in sortedform:",','.join(unique_words))
-------------------------------------------------------------------------------
Output
Enter a comma-separated sequence of words India,America,India,China,America
Unique words in sortedform: America,China,India
