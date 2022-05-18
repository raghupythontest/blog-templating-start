from flask import Flask, render_template
from post import Post

posts=Post()
posts_data=posts.data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=posts_data)

@app.route('/post/<id>')
def getpost(id):
    return render_template("post.html",post=posts_data[int(id)-1])

if __name__ == "__main__":
    app.run(debug=True)
