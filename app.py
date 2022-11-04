import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        store = request.form["store"]
        response = openai.Completion.create(
            model="text-davinci-001",
            prompt=generate_prompt(store),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(store):
    return """Write a tagline for a {}.""".format(
        store)

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')
