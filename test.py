from concept_algorithm import analyze_concepts
from pdf_helper import get_words
from db import upload_document
from db_compare import insert_terms

def get_concepts(filename):
    return analyze_concepts(get_words(filename)[1])

def upload(filename):
    words = get_words(filename)
    content = words[0]
    analysis = analyze_concepts(words[1])
    concepts = [a.name() for a in analysis]
    keywords = dict()
    for word in content:
        if word in keywords:
            keywords[word] += 1
        else:
            keywords[word] = 1
    upload_document(concepts, filename, "test", "test", "test", keywords, words[2])

def upload_term(filename):
    words = get_words(filename)
    word_count = words[2]
    insert_terms(word_count, filename)

def compare_searches():
    pass