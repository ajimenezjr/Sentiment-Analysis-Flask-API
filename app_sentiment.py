import nltk
from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)
output = {}


def sentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)['compound']
    if score > 0:
        return "Positive"
    else:
        return "Negative"


@app.route("/", methods=["GET", "POST"])
def sentiment_request():
    if request.method == "POST":
        sentence = request.form['q']
        sent = sentiment(sentence)
        output['sentiment'] = sent
        return jsonify(output)
    else:
        sentence = request.args.get('q')
        sent = sentiment(sentence)
        print(sentence)
        output['sentiment'] = sent
        return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)

print(__name__)
