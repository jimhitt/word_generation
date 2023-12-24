import nltk
import re
from collections import Counter
from nltk.corpus import stopwords
import spacy as spaCy
#nltk.download('punkt')

# open named entity recognition model
nlp = spaCy.load('en_core_web_sm')

# Function to process the file
def process_file(file_path, nlp = nlp):
    # open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # use spaCy to process the text and find named entities
    doc = nlp(text)

    named_entities = set()

    for ent in doc.ents:
        named_entities.add(ent.text.lower().strip())
    
    # Tokenize the text
    words = re.findall(r'\b\w+\b', text.lower())

    # remove stopwords
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]

    # keep only words that are alphabetic and not empty
    words = [word for word in words if word.isalpha() and len(word) > 0]

    # filter out words that are not 'PERSON' named entities
    person_entities = set()
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            person_entities.add(ent.text.lower().strip())
    
    # filter out person entities from words
    filtered_words = [word for word in words if word not in person_entities]

    # Count the words
    word_count = Counter(filtered_words)

    # Count named entities
    named_words = [word for word in words if word in person_entities]
    word_count_named_entities = Counter(named_words)

    return word_count, word_count_named_entities

txt_file_path = './text_files/huckleberry_fin.txt'
word_count, word_count_named_entities = process_file(txt_file_path)

# print 25 most common named entities
for word, count in word_count_named_entities.most_common(25):
    print(f"{word}: {count}")

print(f"{'-'*45}")

# print 25 most common words
for word, count in word_count.most_common(25):
    print(f"{word}: {count}")