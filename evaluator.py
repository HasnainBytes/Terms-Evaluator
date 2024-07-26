import nltk
from collections import Counter

nltk.download('punkt')

def read_terms(file_path):
    with open(file_path, 'r') as file:
        terms = file.read()
    return terms

def evaluate_terms(terms):
    unsafe_keywords = [
        "waive", "liability", "dispute", "binding", "arbitration", "third-party",
        "tracking", "data collection", "no refund", "no liability", "disclaimer",
        "indemnify", "automatic renewal", "termination"
    ]
    words = nltk.word_tokenize(terms.lower())
    keyword_counts = Counter(word for word in words if word in unsafe_keywords)
    total_keywords = sum(keyword_counts.values())
    safe_count = len(words) - total_keywords
    return {
        'safe': safe_count,
        'not_safe': total_keywords,
        'keyword_counts': keyword_counts
    }