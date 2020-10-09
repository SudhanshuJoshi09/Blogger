# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

doc = nlp("Hello world!")

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)
