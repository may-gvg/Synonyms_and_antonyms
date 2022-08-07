import nltk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
import requests
import json


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()


with open("test.json", "r") as file:
    data = json.load(file)

print(data['sentences'])
print(data['sentences'][2])
print(data['sentences'][0]['sentiment']['type'])

response = requests.get("https://www.poemist.com/api/v1/randompoems")
data_from_json = response.json()

# synonyms = []
# for syn in wordnet.synsets("travel"):
#     for lm in syn.lemmas():
#         synonyms.append(lm.name())  # adding into synonyms
# print(set(synonyms))
#
# antonyms = []
# for syn in wordnet.synsets("increase"):
#     for lm in syn.lemmas():
#         if lm.antonyms():
#             antonyms.append(lm.antonyms()[0].name())  # adding into antonyms
# print(set(antonyms))
#
# words = ['amazing', 'interesting', 'love', 'great', 'nice', "Mike"]
#
# for w in words:
#     tmp = wn.synsets(w)[0].pos()
# print(w, ":", tmp)
#
# lemmatizer = nltk.WordNetLemmatizer()
#
# # word tokenizeing and part-of-speech tagger
# document = 'The little brown dog barked at the black cat'
# tokens = [nltk.word_tokenize(sent) for sent in [document]]
# postag = [nltk.pos_tag(sent) for sent in tokens][0]
#
# # Rule for NP chunk and VB Chunk
# grammar = r"""
#     NBAR:
#         {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
#         {<RB.?>*<VB.?>*<JJ>*<VB.?>+<VB>?} # Verbs and Verb Phrases
#
#     NP:
#         {<NBAR>}
#         {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
#
# """
# # Chunking
# cp = nltk.RegexpParser(grammar)
#
# # the result is a tree
# tree = cp.parse(postag)
#
#
# def leaves(tree):
#     """Finds NP (nounphrase) leaf nodes of a chunk tree."""
#     for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
#         yield subtree.leaves()
#
#
# def get_word_postag(word):
#     if pos_tag([word])[0][1].startswith('J'):
#         return wordnet.ADJ
#     if pos_tag([word])[0][1].startswith('V'):
#         return wordnet.VERB
#     if pos_tag([word])[0][1].startswith('N'):
#         return wordnet.NOUN
#     else:
#         return wordnet.NOUN
#
#
# def normalise(word):
#     """Normalises words to lowercase and stems and lemmatizes it."""
#     word = word.lower()
#     postag = get_word_postag(word)
#     word = lemmatizer.lemmatize(word, postag)
#     return word
#
#
# def get_terms(tree):
#     for leaf in leaves(tree):
#         terms = [normalise(w) for w, t in leaf]
#         yield terms
#
#
# terms = get_terms(tree)
#
# features = []
# for term in terms:
#     _term = ''
#     for word in term:
#         _term += ' ' + word
#     features.append(_term.strip())
# print(features)



