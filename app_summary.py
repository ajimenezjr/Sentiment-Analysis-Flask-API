from flask import Flask, render_template, abort, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from summa import summarizer

app = Flask(__name__)
output = {}


def summary_of(sentence, target_length=50):
    # Set the target length for the summary
    # target_length = 700

    # Initialize the summary
    summary = sentence

    # Set the initial ratio value
    ratio = 0.9
    print('Starting Length (words):')
    print(len(summary.split()))
    approved_summary = summary

    # Keep summarizing until the summary is the desired length
    while len(summary.split()) > target_length:
        # Generate a summary with the current ratio value
        summary = summarizer.summarize(summary, ratio=ratio)
        if len(summary.split()) > 0:
            approved_summary = summary
        print(len(approved_summary.split()))
        # Decrease the ratio value
        # ratio -= 0.1

    # Print the summary
    print('Final Length (words):')
    print(len(approved_summary.split()))
    # print(summary)
    return approved_summary


# @app.route("/summary/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def summary_request():
    if request.method == "POST":
        sentence = request.form['q']
        sent = summary_of(sentence)
        output = sent
        return jsonify(output)
    else:
        sentence = request.args.get('q')
        if type(int(request.args.get('words'))) == int:
            target_length_local = request.args.get('words')
        else:
            target_length_local = 50

        sent = summary_of(sentence, int(target_length_local))
        # print(sentence)
        output = sent
        return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)

print(__name__)
