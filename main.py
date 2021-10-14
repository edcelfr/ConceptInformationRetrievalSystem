from flask import Flask, render_template, url_for, redirect, request, jsonify, send_from_directory
from wordnet_helper import get_concepts
from db import get_documents, add_view
from analysis_thread import AnalysisThread

app = Flask(__name__, static_folder="static")

get_concepts("")

#@app.route("/query", methods=["GET", "POST"])
#def query():
    #if request.method == "POST":
        #keywords = request.form["keywords"].split("-")
        #data = []
        #for i in range(len(keywords)):
            #data.append([])
            #concepts = get_concepts(keywords[i])
            #for j in range(len(concepts)):
                #data[i].append((concepts[j].name(), concepts[j].definition()))
        #return jsonify(data)
    
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        if "authors" in request.args:
            authors = request.args["authors"].split("-")
        else:
            authors = []
        documents = get_documents(request.args["concept"].split("-"), authors, request.args["sort"])
        return render_template("results.html", documents=documents)

@app.route("/open")
def open_pdf():
    filename = request.args["filename"]
    add_view(filename)
    return send_from_directory(app.static_folder, "documents/" + filename)

#tests

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-concepts-list", methods=["POST"])
def get_concepts_list():
    if request.method == "POST":
        keyword = request.form["keyword"]
        print(keyword)
        data = []
        concepts = get_concepts(keyword)
        for j in range(len(concepts)):
            data.append((concepts[j].name(), concepts[j].definition()))
        return jsonify(data)

@app.route("/login")
def log():
    return render_template("login.html")

@app.route("/register")
def reg():
    return render_template("register.html")

@app.route("/res")
def res():
    return render_template("results.html")

@app.route("/up", methods=["GET", "POST"])
def up():
    if request.method == "GET":
        return render_template("upload.html")
    if request.method == "POST":
        f = request.files["filename"]
        title = request.form["title"]
        author = request.form["author"]
        college = request.form["college"]
        f.save("static/documents/" + f.filename)
        t = AnalysisThread(f.filename, title, author, college)
        t.start()
        return render_template("upload.html")

@app.route("/admin")
def admin():
    return render_template("admin-profile.html")

@app.route("/student")
def student():
    return render_template("student-profile.html")

@app.route("/advanced")
def advanced_search():
    return render_template("advanced-search.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")