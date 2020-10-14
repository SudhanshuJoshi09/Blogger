import spacy


nlp = spacy.load("en_core_web_sm")

doc = nlp("I love coffee")


#------------------------------------------------------------------
print('About vocab', '*'*50)
coffee_hash = nlp.vocab.strings["coffee"]
print("hash_value: ", coffee_hash)
coffee_string = nlp.vocab.strings[coffee_hash]
print("String: ", coffee_string)
print("Ends Here", '*'*50)
#------------------------------------------------------------------
doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]
# Print the lexical attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
print("Ends Here", '*'*50)
#------------------------------------------------------------------
