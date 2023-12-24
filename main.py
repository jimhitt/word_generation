import nltk
import re
from collections import Counter
from nltk.corpus import stopwords
#nltk.download('punkt')

txt_file_path = './text_files/peter_pan.txt'

# Function to process the file
def process_file(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    words = re.findall(r'\b\w+\b', text.lower())

    # remove stopwords
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]

    # Count the words
    word_count = Counter(words)

    return word_count

word_count = process_file(txt_file_path)

for word, count in word_count.most_common(100):
    print(f"{word}: {count}")

print(len(word_count))

print(f"{'-'*45}")
five_letter_words = {word: count for word, count in word_count.items() if len(word) == 5}

# make sorted dictionary
sorted_dict = {k: v for k, v in sorted(five_letter_words.items(), key=lambda item: item[1], reverse=True)}

# print 50 most common 5 letter words
for word, count in list(sorted_dict.items())[:50]:
    print(f"{word}: {count}")

print(f"{'-'*45}")
print('Number of 5 letter words: ',len(five_letter_words))
