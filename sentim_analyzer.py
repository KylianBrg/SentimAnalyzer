import nltk
nltk.download('vader_lexicon')

from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialisation de l'analyseur de sentiments
sia = SentimentIntensityAnalyzer()

@app.route('/analyse_sentiment', methods=['POST'])
def analyse_sentiment():
    # Récupérer le texte à analyser depuis la requête POST
    data = request.get_json()
    text = data['text']

    # Analyse du sentiment
    sentiment_score = sia.polarity_scores(text)
    
    # Détermination du sentiment en fonction du score
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'positif'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'négatif'
    else:
        sentiment = 'neutre'

    # Création de la réponse JSON
    response = {
        'texte': text,
        'sentiment': sentiment
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
