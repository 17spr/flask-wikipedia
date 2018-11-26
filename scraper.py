import wikipedia
from flask import Flask

app = Flask(__name__)

# search wikipedia
search = wikipedia.search("Flask framework")

# store only the first article found
first_article = search[0]
print(first_article)

# get short summary
summary = wikipedia.summary(first_article, sentences=1)
print(summary)

@app.route('/')
def hello_world():
    return summary
if __name__ == '__main__':
    app.run(port='5000')
