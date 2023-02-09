from flask import Flask

app = Flask(__name__)

indexFile = open("./html/index.html", "r", encoding="UTF-8")
indexContent = indexFile.read()
indexFile.close()

@app.route("/")
def index():
    return indexContent
