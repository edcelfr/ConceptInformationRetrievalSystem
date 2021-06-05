[TO TEST]

Make sure the following packages are installed:
- nltk (3.6.2): "pip install nltk"
- pdfminer (20191125): "install pdfminer"

Upon having nltk installed:
- Run Python's interactive mode on Command Prompt on Windows or its equivalent on another operating system
- Enter "import nltk" and "nltk.download()" in order
- Click "Download"

To test after all previous steps:
- Run the main Python file in interactive mode with "python -i main.py"
- Type in "[variable_name] = analyze_concepts('[file_name].pdf')"
- Wait for the analysis to finish, and your concepts should be stored in [variable_name]
- View concepts (they are sorted in order of relevance within document) by typing in "[variable_name]"