[TO TEST]

Make sure the following packages are installed:
- nltk (3.6.2): "pip install nltk"
- pdfminer (20191125): "install pdfminer"
- flask: "install flask"

Upon having nltk installed:
- Run Python's interactive mode on Command Prompt on Windows or its equivalent on another operating system
- Enter "import nltk" and "nltk.download()" in order
- Click "Download"

To test concept extraction after all previous steps:
- Run the main Python file in interactive mode with "python -i test.py" in Command Prompt.
- Type in "[variable_name] = analyze_concepts('[file_name].pdf')"
- Wait for the analysis to finish, and your concepts should be stored in [variable_name]
- View concepts (they are sorted in order of relevance within document) by typing in "[variable_name]"

To test comparisons between concept matching algorithm and term matching algorithm:
- If you are just about to start, type in "python -i db.py" while the project is open in Command Prompt.
- Type "init_db()" then press Enter to initialize the database.
- Type "quit()" then press Enter to exit the interactive prompt.
- When back in Command Prompt, type in "python -i test.py" then press Enter.
- When in interactive mode, type in "upload("File/Location/Here.pdf")" then press Enter to upload files.
- When you have uploaded as many files as you wish, type "quit()" then press Enter to exit the interactive prompt.
- When back in Command Prompt, type in "python -i db.py" then press Enter.
- Make sure to have the application's homepage running while testing so you can quickly get definitions.
- To run the server, make sure you have another separate Command Prompt open in the same folder, then type in "set FLASK_APP=main.py", then press Enter, then type in "flask run", then press Enter. To see what routes you can open with "localhost:5000", check main.py for routes that start with "app.route("/route-here")". You can open the pages with "localhost:5000/route-here" in your browser's URL bar.
- When in interactive mode, type in "get_documents(["concepts.n.01", "go.n.02", "here.n.01"], [])" to get all documents that contain the concepts in the entered list. To get the concepts you want to search for, type the word you want to get the concepts for in the search bar in homepage. Typing "cat", for example, gets you concepts like "cat.n.01", "cat.n.02", and more, along with their definitions at the side.
- When in interactive mode, type in "get_documents_by_term(["terms", "go", "here"])" to get all documents that contain the words in the entered list.
- Search results will also print out the time taken right under it.
- Record data as you see fit.