# word_generation
Playing with various NLP tools to create word lists for word games. This is not a functional tool but more exploration of NLP techniques.

Currently, I am using text from books found on Project Gutenberg (hand picked)

## Current status

- main.py
  - Use NLKT to remove stop words
  - Finding any word and tokenizing (not worrying about paragraphs or sentences)
  - Using Counter to perform word counts
  - Creating a dictionary of words with specific lengths
  - Noticed that it was including common proper names
- jh_spacy.py
  - Trying spaCy to extract named entities.
  - The named entity class is too broad
  - Trying named entity if ent.label_ == 'PERSON', but this is still broad and misses clear names
- Will explore other NLP tools next

