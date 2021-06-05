from nltk.corpus import wordnet as wn

# for consistency with project description and themes, WordNet's "synset" will be referred to as "concept"

def get_concepts(word):
    # syntactic sugar for WordNet convenience
    return wn.synsets(word.replace(" ", "_"), "n")

def get_lemmas(concept):
    # get all lemmas that are can be used to refer to concept
    return remove_underscores([lemma.name() for lemma in concept.lemmas()])

def get_siblings(concept):
    # get all concepts under a concept's hypernym if any hypernym exists
    siblings = []
    hypernyms = concept.hypernyms() + concept.instance_hypernyms()
    if len(hypernyms) > 0:
        for hypernym in hypernyms:
            siblings.extend(hypernym.hyponyms() + hypernym.instance_hyponyms())
    if concept in siblings:
        siblings.remove(concept)
    return siblings

def get_sibling_lemmas(concept):
    # get string representations of lemmas of siblings
    siblings = []
    for sibling in get_siblings(concept):
        for lemma in sibling.lemmas():
            siblings.append(lemma.name())
    return remove_underscores(siblings)

def get_meronyms(concept):
    # get all concepts that might be part of the concept
    return concept.part_meronyms() + concept.substance_meronyms() + concept.member_meronyms()

def get_meronym_lemmas(concept):
    # get string representations of meronyms
    meronyms = []
    for meronym in concept.part_meronyms() + concept.substance_meronyms() + concept.member_meronyms():
        for lemma in meronym.lemmas():
            meronyms.append(lemma.name())
    return remove_underscores(meronyms)

def get_holonyms(concept):
    # get all concepts that the concept might be part of
    return concept.part_holonyms() + concept.substance_holonyms() + concept.member_holonyms()

def get_holonym_lemmas(concept):
    # get string representations of holonyms
    holonyms = []
    for holonym in concept.part_holonyms() + concept.substance_holonyms() + concept.member_holonyms():
        for lemma in holonym.lemmas():
            holonyms.append(lemma.name())
    return remove_underscores(holonyms)

def get_hypernyms(concept):
    # get all concepts that may be generalizations of the concept
    return concept.hypernyms() + concept.instance_hypernyms()

def get_hypernym_lemmas(concept):
    # get string representations of hypernyms
    hypernyms = []
    for hypernym in concept.hypernyms():
        for lemma in hypernym.lemmas():
            hypernyms.append(lemma.name())
    return remove_underscores(hypernyms)

def get_hyponyms(concept):
    # get all concepts that may be specializations of the concept
    return concept.hyponyms() + concept.instance_hyponyms()

def get_hyponym_lemmas(concept):
    # get string representations of hyponyms
    hyponyms = []
    for hyponym in concept.hyponyms():
        for lemma in hyponym.lemmas():
            hyponyms.append(lemma.name())
    return remove_underscores(hyponyms)

def remove_underscores(lemmas):
    # from a list of words/lemmas, remove underscores and replace with spaces for use in text analysis
    for i in range(len(lemmas)):
        lemmas[i] = lemmas[i].replace("_", " ")
    return lemmas

def get_original_word(concept):
    # get the original lemma of a concept
    word = ""
    for letter in concept.name():
        if letter == ".":
            break
        word += letter
    return word

def get_related_concepts(concept):
    return get_meronyms(concept)\
         + get_holonyms(concept)\
         + get_hypernyms(concept)\
         + get_hyponyms(concept)\
         + get_siblings(concept)

def get_related_lemmas(concept):
    return get_synonyms(concept)\
         + get_meronym_lemmas(concept)\
         + get_holonym_lemmas(concept)\
         + get_hypernym_lemmas(concept)\
         + get_hyponym_lemmas(concept)