from wordnet_helper import *
from concept_tree_set import ConceptTreeSet
import time

def analyze_concepts(content, words):
    # start_time used in operation later for benchmarking purposes
    start_time = time.time()
    concepts = [concept for word in words for concept in get_concepts(word)]
    concept_trees = [ConceptTreeSet(get_concepts(word)) for word in words if len(get_concepts(word)) > 0]
    for concept_tree in concept_trees:
        for concept in concepts:
            concept_tree.add_concept(concept)
        for word in content:
            concept_tree.add_word(word)
    estimated_concepts = dict()
    for concept_tree in concept_trees:
        if concept_tree.get_highest_accuracy() > 0:
            estimated_concepts[concept_tree.get_most_accurate_concept()] = concept_tree.get_most_accurate_concept_relevance()
    print(str(time.time() - start_time))
    return dict(sorted(estimated_concepts.items(), key=lambda item:item[1]))