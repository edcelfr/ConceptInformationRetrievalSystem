from pdf_helper import get_words
from concept_algorithm import *

def analyze_document(file_name):
    words = get_words(file_name)
    return analyze_concepts(words[0], words[1])