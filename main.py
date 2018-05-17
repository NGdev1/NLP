# coding=utf-8
import string
import functions
from nltk.tokenize import word_tokenize

if __name__ == '__main__':

    twits_file = open("tweets_Id.txt", "r")

    line = ""
    lines_array = []
    while 1:
        line = twits_file.readline()
        if line == "":
            break
        lines_array.append(line)

    twits_dictionary = {}
    twits_array = []
    for item in lines_array:
        array = string.split(item, '\t')
        twits_dictionary[array[0]] = array[1]
        twits_array.append(array[1])

    twits = [functions.remove_all_punctuation_and_nicknames(functions.remove_all_links(twit.lower())) for twit in twits_array]
    twits_tokens = [functions.append_stemming(functions.remove_stopwords(word_tokenize(doc))) for doc in twits]

    # tf - term frequency - частота токена
    tokens = set()
    words_count = 0

    for twit_tokens in twits_tokens:
        for token in twit_tokens:
            tokens.add(token)
            words_count += 1

    file_statistics = open('statistics.txt', 'w+')
    file_result = open('result.txt', 'w+')

    file_statistics.write("Documents count: " + str(len(twits_array)))
    file_statistics.write("\n")
    file_statistics.write("Words count: " + str(words_count))
    file_statistics.write("\n")
    file_statistics.write("Unique words count: " + str(len(tokens)))

    for item in tokens:
        file_result.write(item + '\n')
