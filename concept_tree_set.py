from wordnet_helper import *
from concept_tree import ConceptTree
from nltk.corpus import wordnet as wn

class ConceptTreeSet:

    # this class will be used for determine which concept from a list of concepts is most appropriate
    # within the document based on relationships with concepts that may exist in the document

    def __init__(self, concepts):
        self.concepts = [ConceptTree(concept) for concept in concepts]
        self.acquired_lemmas = [set() for i in range(len(concepts))]
        self.acquired_siblings = [set() for i in range(len(concepts))]
        self.acquired_hyponyms = [set() for i in range(len(concepts))]
        self.acquired_hypernyms = [set() for i in range(len(concepts))]
        self.acquired_meronyms = [set() for i in range(len(concepts))]
        self.acquired_holonyms = [set() for i in range(len(concepts))]
        self.lemma_frequency = [0 for i in range(len(concepts))]

    def add_concept(self, concept):
        for i in range(len(self.concepts)):
            if (concept in self.concepts[i].hyponyms):
                self.acquired_hyponyms[i].add(concept)
            elif (concept in self.concepts[i].hypernyms):
                self.acquired_hypernyms[i].add(concept)
            elif (concept in self.concepts[i].meronyms):
                self.acquired_meronyms[i].add(concept)
            elif (concept in self.concepts[i].holonyms):
                self.acquired_holonyms[i].add(concept)
            elif (concept in self.concepts[i].siblings):
                self.acquired_siblings[i].add(concept)

    def add_concepts(self, concepts):
        for concept in concepts:
            self.add_concept(concept.concept)

    def add_word(self, lemma):
        for i in range(len(self.concepts)):
            if lemma in self.concepts[i].lemmas:
                self.acquired_lemmas[i].add(lemma)
                self.lemma_frequency[i] += 1

    def get_accuracy(self, index):
        #acc = 0
        #if (len(self.acquired_hypernyms[index]) > 0):
            #acc += 0.2
        #if (len(self.acquired_hyponyms[index]) > 0):
            #acc += 0.2
        #if (len(self.acquired_meronyms[index]) > 0):
            #acc += 0.2
        #if (len(self.acquired_holonyms[index]) > 0):
            #acc += 0.2
        #if (len(self.acquired_siblings[index]) > 0):
            #acc += 0.2
        #return round(acc, 2)
        return len(self.acquired_hypernyms[index]) +\
                len(self.acquired_hyponyms[index]) +\
                len(self.acquired_meronyms[index]) +\
                len(self.acquired_holonyms[index]) +\
                len(self.acquired_siblings[index])

    def get_relevance_score(self, index):
        return round(self.get_accuracy(index) * self.lemma_frequency[index], 2)

    def get_most_accurate_concept(self):
        highest_accuracy = 0
        highest_index = 0
        for i in range(len(self.concepts)):
            if self.get_accuracy(i) > highest_accuracy:
                highest_accuracy = self.get_accuracy(i)
                highest_index = i
        return self.concepts[highest_index].concept

    def get_most_accurate_concept_relevance(self):
        highest_accuracy = 0
        highest_index = 0
        for i in range(len(self.concepts)):
            if self.get_accuracy(i) > highest_accuracy:
                highest_accuracy = self.get_accuracy(i)
                highest_index = i
        return self.get_relevance_score(highest_index)

    def get_highest_accuracy(self):
        highest = 0
        for i in range(len(self.concepts)):
            if self.get_accuracy(i) > highest:
                highest = self.get_accuracy(i)
        return highest

    def get_highest_frequency(self):
        highest = 0
        for i in range(len(self.concepts)):
            if self.lemma_frequency[i] > highest:
                highest = self.lemma_frequency[i]
        return highest

    def get_highest_relevance(self):
        highest = 0
        for i in range(len(self.concepts)):
            if self.get_relevance_score(i) > highest:
                highest = self.get_relevance_score(i)
        return highest

    def get_most_relevant_concept(self):
        highest_score = 0
        highest_index = 0
        for i in range(len(self.concepts)):
            if self.get_relevance_score(i) > highest_score:
                highest_score = self.get_relevance_score(i)
                highest_index = i
        return self.concepts[highest_index].concept

    def get_most_relevant_concept_stats(self):
        highest_score = 0
        highest_index = 0
        for i in range(len(self.concepts)):
            if self.get_relevance_score(i) > highest_score:
                highest_score = self.get_relevance_score(i)
                highest_index = i
        return str(self.get_accuracy(highest_index)) + " * " + str(self.lemma_frequency[highest_index]) + " = " + str(self.get_relevance_score(highest_index))