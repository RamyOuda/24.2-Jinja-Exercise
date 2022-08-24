from stories import story
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home_page():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def story_page():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
