#Task 1
import re
files = ["C:/Users/Chari/WorkspacePY/NLP/Exercise 2/reviews1.txt", "C:/Users/Chari/WorkspacePY/NLP/Exercise 2/reviews2.txt", "C:/Users/Chari/WorkspacePY/NLP/Exercise 2/reviews3.txt"]
reviews = []

for file in files:
    try:
        text = open(file, "r", encoding="utf8").read()        
    except UnicodeDecodeError:
        text = open(file, "r", encoding="utf16").read()

    split_reviews = re.split(r'\n\s*\n|<br\s*/?><br\s*/?>', text)

    for r in split_reviews:
        reviews.append(r)
    
print("Task 1:-------------------------------------------------------------------------")
print(reviews)
 

#Task 2
from collections import Counter

preprocessed_reviews = []
all_words = []

for review in reviews:
    #review = review.lower()
    review = re.sub(r'[^a-zA-Z\s]', '', review)
    review = review.lower().split()
    preprocessed_reviews.append(review)

for review in preprocessed_reviews:
    for words in review:
        all_words.append(words)

word_counts = Counter(all_words)

print("Task 2:-------------------------------------------------------------------------")
print(preprocessed_reviews)
print(word_counts.most_common(10))


#Task 3
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('omw-1.4')

ps = PorterStemmer()
wl = WordNetLemmatizer()

stemmed_reviews = []
lemmatized_reviews = []
for review in preprocessed_reviews:
    for word in review:
        stemmed_reviews.append(ps.stem(word))
        lemmatized_reviews.append(wl.lemmatize(word))

print("Task 3:-------------------------------------------------------------------------")
print(stemmed_reviews)
print(lemmatized_reviews)


#Task 4

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

filtered_stop_words = []
for word in stop_words:
    w_clean = re.sub(r'[^a-z]', '', word.lower())
    filtered_stop_words.append(w_clean)

filtered_reviews = []

for word in lemmatized_reviews:
    if word not in filtered_stop_words:
        filtered_reviews.append(word)


word_counts_filtered = Counter(filtered_reviews)

print("Task 4:-------------------------------------------------------------------------")
print(filtered_reviews)
print(word_counts_filtered.most_common(10))

