from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "runner", "running"]

for w in words:
    print(w, "->", stemmer.stem(w))
