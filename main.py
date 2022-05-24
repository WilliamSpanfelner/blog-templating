from flask import Flask, render_template
import requests


class Blog:
    def __init__(self):
        self.all_posts = []

    def get_posts(self):
        blog_url = "https://api.npoint.io/f5ddf11fcc045f6cd8a7"
        response = requests.get(blog_url)
        self.all_posts = response.json()
        return self.all_posts


blog = Blog()
blog_posts = blog.get_posts()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)


@app.route('/post/<blog_id>')
def read_post(blog_id):
    num = int(blog_id) - 1
    return render_template("post.html", post=blog_posts[num])


if __name__ == "__main__":
    app.run(debug=True)
