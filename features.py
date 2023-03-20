import nltk
from nltk.corpus import stopwords
import re, unicodedata
from empath import Empath
from textblob import TextBlob 
import pandas as pd
import string

nltk.download('punkt')
nltk.download('stopwords')
sw_nltk = stopwords.words('english')

def average_token_length(words):
    lengths = [len(i) for i in words]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths))

def longest_token_length(words):
    return max(words, key = len)

def token_count(words):
    return len(words)

def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers'''
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def convert_case(text):
    return text.lower()

def tokenize(text):
    tokens = []
    for line in text.split('\n'):
        tokens.append([word for word in line.strip().split(" ")])
    return tokens

def remove_stop_words(text):
    words = [word for word in text.split() if word.lower() not in sw_nltk]
    new_text = " ".join(words)
    return new_text

def jaccard(str1, str2): 
    a = set(str1.lower().split()) 
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
    
def remove_accents(string):
    nfkd = unicodedata.normalize('NFKD', string)
    return u"".join([c for c in nfkd if not unicodedata.combining(c)])

def empath_finder(poem):
    lexicon = Empath()
    poem_without_eol=''.join([item.rstrip('\n') for item in poem])
    return lexicon.analyze(poem_without_eol, normalize=True)

def get_sentiment( string): 
    analysis = TextBlob(string) 
    return analysis.sentiment.polarity