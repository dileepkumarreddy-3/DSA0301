import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

text = "Natural language processing is very interesting"

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

for t in tags:
    print(t)
