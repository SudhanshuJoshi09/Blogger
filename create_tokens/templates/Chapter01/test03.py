# Attribute Test.
from spacy.lang.en import English

# Create the nlp object
nlp = English()

doc = nlp("It costs $5.")


# Here this token.i is very important.
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
