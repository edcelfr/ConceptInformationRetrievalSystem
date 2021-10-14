import sqlite3 as sql
from wordnet_helper import get_lemmas
from nltk.corpus import wordnet as wn
import time

wn.synsets("")

def init_db():
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE documents (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, college TEXT, views INTEGER, filename TEXT)")
    c.execute("CREATE TABLE concepts (id INTEGER PRIMARY KEY AUTOINCREMENT, concept TEXT, documentID INTEGER)")
    c.execute("CREATE TABLE keywords (id INTEGER PRIMARY KEY AUTOINCREMENT, keyword TEXT, documentID INTEGER, frequency INTEGER)")
    c.execute("CREATE TABLE terms (id INTEGER PRIMARY KEY AUTOINCREMENT, term TEXT, documentID TEXT, frequency INTEGER)")
    c.execute("CREATE TABLE students (id TEXT PRIMARY KEY, fullName TEXT, email TEXT, college TEXT, password TEXT)")
    conn.commit()
    conn.close()

def upload_document(concepts, filename, title, author, college, keywords, word_count):
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO documents (title, author, college, views, filename) VALUES ('" + title + "', '" + author + "', '" + college +"', 0, '" + filename + "')")
    c.execute("SELECT * FROM documents WHERE filename = ?", (filename,))
    id = c.fetchone()[0]
    for concept in concepts:
        c.execute("INSERT INTO concepts (concept, documentID) VALUES ('" + concept + "', " + str(id) + ")")
    for keyword in keywords:
        c.execute("INSERT INTO keywords (keyword, documentID, frequency) VALUES ('" + keyword + "', " + str(id) + ", " + str(keywords[keyword]) + ")")
    for word in word_count:
        c.execute("INSERT INTO terms(term, documentID, frequency) VALUES ('" + word + "', '" + str(id) + "', " + str(word_count[word]) + ")")
    conn.commit()
    conn.close()

def get_documents(concepts, authors, sort_type="relevance"):
    start_time = time.time()
    # TODO: combine concept retrieval with term retrieval
    results = []
    lemmas = []
    count = 0
    for concept in concepts:
        lemmas.extend(get_lemmas(wn.synset(concept)))
    concept_condition = ""
    frequency_condition = ""
    author_condition = ""
    for i in range(len(concepts)):
        if i == 0:
            concept_condition = "documents.id == concepts0.documentID AND concepts0.concept == '" + concepts[i] + "'"
        else:
            count += 1
            concept_condition += " INNER JOIN concepts AS concepts" + str(count) + " ON documents.id == concepts" + str(count) + ".documentID AND concepts" + str(count) + ".concept == '" + concepts[i] + "'"
    for i in range(len(lemmas)):
        if i == 0:
            frequency_condition = "keyword == '" + lemmas[i] + "'"
        else:
            frequency_condition += " OR keyword == '" + lemmas[i] + "'"
    if len(authors) > 0:
        for i in range(len(authors)):
            if i == 0:
                author_condition = " WHERE documents.author == '" + authors[i] + "'"
            else:
                author_condition += " AND documents.author == '" + authors[i] + "'"
    conn = sql.connect("database.db")
    c = conn.cursor()
    for row in c.execute("SELECT title, filename, views FROM documents INNER JOIN concepts AS concepts0 ON " + concept_condition + author_condition + " ORDER BY title"):
        results.append([row[0], row[1], row[2]])
    for i in range(len(results)):
        for row in c.execute("SELECT SUM(frequency) FROM documents INNER JOIN keywords ON documents.id == keywords.documentID WHERE " + frequency_condition + " AND filename == '" + results[i][1] + "'"):
            results[i].append(row[0])
    for i in range(len(results)):
        results[i] = tuple(results[i])
    if sort_type == "views":
        results = sorted(results, key=lambda e: e[2], reverse=True)
    elif sort_type == "relevance":
        results = sorted(results, key=lambda e: e[3], reverse=True)
    conn.commit()
    conn.close()
    print(time.time() - start_time)
    return results

def get_documents_by_term(terms):
    start_time = time.time()
    # keep for copying code to db.py
    conn = sql.connect("database.db")
    c = conn.cursor()
    query = ""
    for i in range(len(terms)):
        if i == 0:
            query = "SELECT terms.term, title, terms.documentID, terms.frequency FROM terms INNER JOIN documents ON terms.documentID = documents.id INNER JOIN terms AS terms0 ON terms.id == terms0.id WHERE terms0.term = '" + terms[i] + "' " 
        else:
            query += "INNER JOIN terms AS terms" + str(i) + " ON terms.id == terms" + str(i) + ".id WHERE terms" + str(i) + ".term = '" + terms[i] + "' " 
    results = []
    for row in c.execute(query):
        results.append(row[1])
    # for testing first
    conn.commit()
    conn.close()
    print(time.time() - start_time)
    return results

def add_view(filename):
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE documents SET views = views + 1 WHERE filename = '" + filename + "'")
    conn.commit()
    conn.close()

def clear_documents():
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM documents")
    conn.commit()
    conn.close()

def clear_concepts():
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM concepts")
    conn.commit()
    conn.close()

def clear_keywords():
    conn = sql.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM keywords")
    conn.commit()
    conn.close()

def get_all_documents():
    results = []
    conn = sql.connect("database.db")
    c = conn.cursor()
    for row in c.execute("SELECT * FROM documents"):
        results.append(row)
    conn.commit()
    conn.close()
    return results