import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
data = "Data science is one of the most important fields in the world."
tokens = word_tokenize(data)
tokens = [word.lower() for word in tokens]
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Original Text:")
print(data)
print("\nTokens after Stopword Removal:")
print(filtered_tokens)
print("\nTokens after Lemmatization:")
print(lemmatized_tokens)