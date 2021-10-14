from wordnet_helper import *
from concept_tree_set import ConceptTreeSet
import time

def analyze_concepts(words):
    # start_time used in operation later for benchmarking purposes
    start_time = time.time()
    concepts = set([tuple(get_concepts(word)) for word in words if len(get_concepts(word)) > 0])
    concept_trees = [ConceptTreeSet(concept) for concept in list(concepts)]
    for i in range(len(concept_trees) - 2):
        for j in range(i + 1, len(concept_trees) - 1):
            concept_trees[i].add_concepts(concept_trees[j].concepts)
            concept_trees[j].add_concepts(concept_trees[i].concepts)
    print(str(time.time() - start_time))
    return sorted([concept_tree.get_most_accurate_concept() for concept_tree in concept_trees], key=lambda item: item.name())