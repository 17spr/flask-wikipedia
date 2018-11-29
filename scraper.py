import wikipedia
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def search_input():
    return render_template('search.html')
# this route will render the results of the user's search
@app.route('/', methods=['POST'])
def search_result():
    # gets the user input from the form in search.html
    text = request.form['text']
    search = wikipedia.search(text)
    first_article = search[0]
    summary = wikipedia.summary(first_article, sentences=1)
    return summary

if __name__ == '__main__':
    app.run()
