# This program follows through the example code of Task 38 of HyperionDev's Software Development Bootcamp.

# Import modules
import spacy

# Load spaCy module
nlp = spacy.load('en_core_web_md')


##### EXAMPLE 1 #####

# Initialise word variables
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Run example comparisons
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

###################### NOTE ######################
# The most interesting feature of this comparison
# is that although cat and monkey are the most 
# similar, monkey and banana are much more similar 
# than cat and banana; thus recognising than 
# although they are distinct, they are related 
# more than a cat and banana are cognitively.
##################################################

print()


##### EXAMPLE 2 #####

# Initialise tokens
tokens = nlp('sleuth sloth fried egg')

# Compare all tokens to each other
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()


##### EXAMPLE 3 #####

# Initialise sentence to compare
sentence_to_compare = "Why is my cat on the car"

# Initialise list of sentences
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

# Prepare sentence for comparison
model_sentence  = nlp(sentence_to_compare)

# Compare test sentence to all other sentences and print results
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity}")