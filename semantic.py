import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# I was surprised that about the difference in similarity between monkey and banana and cat and banana.

# -- My Example --
word1 = nlp("bat")
word2 = nlp("bar")
word3 = nlp("car")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# When I ran the example file, I found out that even though they are being tokenising the same words
# and comparing them, there are still varying levels of similarity implying less accuracy.