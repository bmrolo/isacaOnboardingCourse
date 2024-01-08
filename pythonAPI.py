from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page.<br><br>Here are the following methods you can use: getReposts, getLikes, getBookmarks"

@app.route("/getReposts")
def getReposts():
    repost_data = {
        "Reposts": "100 Reposts"
    }
    return jsonify(repost_data), 200

@app.route("/getLikes")
def getLikes():
    like_data = {
        "Likes": "200 Likes"
    }
    return jsonify(like_data), 200

@app.route("/getBookmarks")
def getBookmarks():
    bookmarks_data = {
        "Bookmarks": "300 Bookmarks"
    }
    return jsonify(bookmarks_data), 200

if __name__ == "__main__":
    app.run(debug=True)