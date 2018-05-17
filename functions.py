import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def print_list(list):
    for item in list:
        print item

def remove_all_links(text):
    text = re.sub(r"http\S+", "", text)
    return  text

def remove_all_punctuation_and_nicknames(text):
    text = re.sub(r"@\S+", "", text)
    text = re.sub(r"#\S+", "", text)
    text = re.sub(r"[0-9]", "", text)
    text = string.replace(text, "d", "")
    text = string.replace(text, "rt", "")

    for punctuationSym in string.punctuation:
        text = text.replace(punctuationSym, ' ')

    return text

def remove_stopwords(array):
    result = []
    for item in array:
        if item not in stopwords.words('english'):
            if len(item) > 2:
                result.append(item)

    return result

def append_stemming(array):
    porter_stemmer = PorterStemmer()

    result = []
    for item in array:
        result.append(porter_stemmer.stem(item))

    return result


def token_term_frequency(word, tokens_all):
    count = 0
    for tokens in tokens_all:
        count += tokens.count(word)

    return count


def token_document_frequency(word, tokens_all):
    count = 0
    for tokens in tokens_all:
        if word in tokens:
            count += 1

    return count
