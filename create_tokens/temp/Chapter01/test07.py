import spacy 


nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buyting U.K. startup for $1 billion.")

for ent in doc.ents:
    print(ent.text, ent.label_)

doc = nlp("Amazon likes Chease, so they bought there Bangalore Headquaters for $1 million. ")

for ent in doc.ents:
    print(ent.text, ent.label_)

print(spacy.explain("GPE"))
print(spacy.explain("NNP"))
print(spacy.explain("dobj"))
