from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import random
from mongos import *

# response = requests.get("...*json")
# data = response.json()

with open("test.json", "r") as file:
    data = json.load(file)


def replace_positive_word(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())  # adding into synonyms
    if len(synonyms) > 0:
        new_word = random.choice(synonyms)
        return new_word
    else:
        return word


def replace_negative_word(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())  # adding into antonyms
    if len(antonyms) > 0:
        new_word = random.choice(antonyms)
        return new_word
    else:
        return word


def replace_sentiment(sentence, polarity):
    print("Old sentence: ")
    print(sentence)
    print("Polarity: " + str(polarity))
    print("Type: " + str(typ))
    sentences = sent_tokenize(sentence)
    json = []
    for line in sentences:
        words_in_each_sentence = word_tokenize(line)
        for i, word in enumerate(words_in_each_sentence):
            if polarity >= 0:
                words_in_each_sentence[i] = replace_positive_word(word)
            else:
                words_in_each_sentence[i] = replace_negative_word(word)
        print("New sentence: ")
        s = TreebankWordDetokenizer().detokenize(words_in_each_sentence)
        json.append({"sentence": s})
        print(s)
        print(" ")
    insert_sentences(json)


for i in data['sentences']:
    sentence = i['sentence']
    sentiment = i['sentiment']
    polarity = sentiment['polarity']
    typ = sentiment['type']
    replace_sentiment(sentence, polarity)
