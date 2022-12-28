import spacy

print("""=======================================================
                        OBSERVATIONS
=======================================================
1. Interesting
Recognised higher correlation across fruits, across animals, and between
animals and fruits that would typically be associated with one another.

My example used rock, cycling and cake.  While it recognised coprrelation between rock
and climbing, vs cycling and climbing was surprised that correlation was not
stronger.

The SM library provided a much less sophisticated analysis, producing less reliable
results, eg monkey/apple stronger than monkey/banana.  It did however identify a
stronger correlation between cycling and cake.  Cyclists do eat a lot of cake!

The SM model also produced a warning ahead of each .similarity() execution explaining
that the results may not be useful as no word vectors are loaded, with the token method
relying instead on the tagger, parser and Named entity recognition.


In Task 37 I was surprised that the NER engine did not identify ducks and oceans as
types of entity, which helps to explain some of the results below.

The sentence correlations using the MD model feel much more complex also, it seems to
know that the subject matter is about the location of something in relation to a car - with
the SM model concentrating more on the similarity of the words amking up the sentences.

---------------------------------------------------------
EXERCISES >>>
---------------------------------------------------------

""")

# Heading
print("""=======================================================
                        MD MODEL
=======================================================""")

# Load md library into spacy
nlp = spacy.load('en_core_web_md')

# Run word comparisons through similarity method in spacy
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Tokenise string and run tokens through similarity method in spacy
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

tokens = nlp('climbing rock cycling cake ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Run sentences through comparison method in spacy.
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",  similarity)

# Heading
print("""=======================================================
                        SM MODEL
=======================================================""")

# Load sm library through spacy
nlp = spacy.load('en_core_web_sm')

# Run word comparisons through similarity method in spacy
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Tokenise string and run tokens through similarity method in spacy
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

tokens = nlp('climbing rock cycling cake ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Run sentences through comparison method in spacy.
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",  similarity)
