import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    # Text of the token.
    token_text = token.text

    # This is for the part of speech.
    token_pos = token.pos_

    # This is for the label.
    token_dep = token.dep_

    # This is for formatting only
    # This formatting is important.
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
