import spacy

from spacy.matcher import Matcher


nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

matcher.add("FIFA", None, pattern)

doc = nlp("2018 FIFA World Cup: France won!")

matches = matcher(doc)

for match_id, start, end in matches:
    print(doc[start:end].text)


pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]

matcher.add("LOVE", None, pattern)

doc = nlp("I loved dogs but now I love cats more.")

matches = matcher(doc)


for match_id, start, end in matches:
    print(doc[start:end].text)


pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]

matcher.add("BUY", None, pattern)

doc = nlp("I bought a smartphone. Now I'm buying apps.")

matches = matcher(doc)


for match_id, start, end in matches:
    print(doc[start:end].text)

