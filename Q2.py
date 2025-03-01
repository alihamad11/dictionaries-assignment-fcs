string = input("write a sentence...")

#split the words in a sentence
words = string.split()

wordsCount = {}

for word in words:
    wordsCount[word] = wordsCount.get(word, 0) + 1

print (wordsCount)