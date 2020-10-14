# SPAN

# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

doc = nlp("Hello world!")

# Index into the Doc to get a single Token
span = doc[1:3]

# Get the token text via the .text attribute
print(span.text)
