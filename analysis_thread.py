import threading
from db import upload_document
from pdf_helper import get_words
from concept_algorithm import analyze_concepts

lock = threading.Lock()

class AnalysisThread(threading.Thread):

    def __init__(self, filename, title, author, college):
        threading.Thread.__init__(self)
        self.filename = filename
        self.title = title
        self.author = author
        self.college = college

    def run(self):
        lock.acquire()
        words = get_words("static/documents/" + self.filename)
        content = words[0]
        analysis = analyze_concepts(words[1])
        concepts = [a.name() for a in analysis]
        upload_document(concepts, self.filename, self.title, self.author, self.college, words[2])
        lock.release()