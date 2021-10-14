import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def get_words(filename):
    print("Preparing necessary objects...")
    # PDF object preparation
    output_string = StringIO()
    with open(filename, "rb") as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        print("Parsing PDF...")
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    lemmatizer = WordNetLemmatizer()
    words = []
    word_count = {}
    print("Getting words...")
    for word in nltk.word_tokenize(output_string.getvalue()):
        # word_tokenize(str) automatically removes all punctuation marks
        if word.isalpha() and word.lower() not in stopwords.words("english") and word.isascii() and len(word) > 1:
            # checks if current word in document is:
            # - completely alphabetical
            # - not a stopword (is, are, the, etc.)
            # - is in ASCII encoding
            words.append(word)
            lemma = lemmatizer.lemmatize(word).lower()
            # lemmatize the word (return to base form)
            if lemma in word_count:
                word_count[lemma] += 1
            else:
                word_count[lemma] = 1
            # word count required for term frequency database

    bigrams = []
    # bigrams: compound words made from 2 words

    print("Getting bigrams...")
    for i in range(len(words) - 1):
        # simply combine all words by pairs from words list previously created
        bigrams.append(words[i] + " " + words[i + 1])

    trigrams = []

    print("Getting trigrams...")
    for i in range(len(words) - 2):
        # same as bigram but 3 words at a time
        trigrams.append(words[i] + " " + words[i + 1] + " " + words[i + 2])
   
    print("Content and unique words parsed.")
    # returns list [X, Y, Z] where:
    # X: all valid words and bigrams in document in order (includes duplicates)
    # Y: all unique words and bigrams in document (no duplicates)
    # Z: words and their respective frequencies (no duplicates)
    return [words + bigrams + trigrams, set(words).union(set(bigrams)).union(set(trigrams)), word_count]