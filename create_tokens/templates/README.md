# Spacy Notes

Spacy is a python Natural Language Processing **(NLP)** which is mostly used for data processing.

## Installation

Use pip package manager to install Spacy.

```bash
pip3 install spacy
```

## Usage

```python
import spacy.lang.en import English # English class imported.

nlp = English() 
doc = nlp("Hello, World!")

for token in doc:
  print(token.text, end=' ')

# Output :: 'Hello , World !'
```

## Chapter - 1
- document
- spans
- tokens
- Lexical Attributes
