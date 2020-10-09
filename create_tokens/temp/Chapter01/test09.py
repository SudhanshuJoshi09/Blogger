import spacy


# Import to Matcher class.
from spacy.matcher import Matcher


# Load the model and create the object.
nlp = spacy.load("en_core_web_sm")


# Initilaize the matcher with the shared verb.
matcher = Matcher(nlp.vocab)


# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)


# Call the matcher on the doc
doc = nlp("Upcoming iPhone X release date leaked")
matches = matcher(doc)


# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)
