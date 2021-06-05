from wordnet_helper import *

class ConceptTree:

    # a Concept Tree is a data structure, specifically a variation of the graph data structure
    # where in a single central vertex contains a synonym set (concept) of a specific word
    # and is connected by edges to other separate vertices that contain sets of related concepts
    # CONCEPT: disambiguation - "orange" disambiguated as the color orange is a synonym set under "orange"
    # HYPERNYMS: generalizations of a concept - "feline" is a hypernym of "tiger"
    # HYPONYMS: specialization of a concept - "tiger" is a hyponym of "feline"
    # MERONYM: parts of a concept - "arm", "chest", and "belly" are meronyms of "torso"
    # HOLONYM: a whole that a concept is a part of -"car" is a holonym of "wheel"
    # SIBLINGS: other hyponyms under a concept's hypernym - "apple" and "mango" are siblings of "orange" under "fruit"

    def __init__(self, synset):
        self.concept = synset
        self.lemmas = get_lemmas(synset)
        self.siblings = get_siblings(synset)
        self.hypernyms = get_hypernyms(synset)
        self.hyponyms = get_hyponyms(synset)
        self.meronyms = get_meronyms(synset)
        self.holonyms = get_holonyms(synset)