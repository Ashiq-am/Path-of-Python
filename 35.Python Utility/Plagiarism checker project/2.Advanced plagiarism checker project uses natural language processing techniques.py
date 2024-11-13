import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to preprocess the text
def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Stem the words
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    # Join the stemmed words
    preprocessed_text = " ".join(stemmed_tokens)

    return preprocessed_text

# Function to compare two texts
def check_plagiarism(file1, file2):
    # Read the contents of the two files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Preprocess the texts
    text1 = preprocess(text1)
    text2 = preprocess(text2)

    # Create a tf-idf vectorizer
    vectorizer = TfidfVectorizer()

    # Create a tf-idf matrix for each text
    tfidf1 = vectorizer.fit_transform([text1])
    tfidf2 = vectorizer.transform([text2])

    # Calculate the cosine similarity
    similarity = cosine_similarity(tfidf1, tfidf2)[0][0]

    # Print the similarity score
    print(f"Similarity score: {similarity}")

# Example usage
check_plagiarism("file1.txt", "file2.txt")