import sqlite3 as sql

def init_db():
    conn = sql.connect("tfidf.db")
    c = conn.cursor()
    c.execute("CREATE TABLE terms (id INTEGER PRIMARY KEY AUTOINCREMENT, term TEXT, document TEXT, frequency INTEGER)")
    conn.commit()
    conn.close()

def insert_terms(word_count, filename):
    conn = sql.connect("tfidf.db")
    c = conn.cursor()
    for word in word_count:
        c.execute("INSERT INTO terms(term, document, frequency) VALUES ('" + word + "', '" + filename + "', " + str(word_count[word]) + ")")
    conn.commit()
    conn.close()

def get_documents(terms):
    # keep for copying code to db.py
    conn = sql.connect("tfidf.db")
    c = conn.cursor()
    query = ""
    for i in range(len(terms)):
        if i == 0:
            query = "SELECT terms.term, terms.document, terms.frequency FROM terms INNER JOIN terms AS terms0 ON terms.id == terms0.id WHERE terms0.term = '" + terms[i] + "' " 
        else:
            query += "INNER JOIN terms AS terms" + str(i) + " ON terms.id == terms" + str(i) + ".id WHERE terms" + str(i) + ".term = '" + terms[i] + "' " 
    results = []
    for row in c.execute(query):
        results.append(row[1])
    # for testing first
    conn.commit()
    conn.close()
    return results