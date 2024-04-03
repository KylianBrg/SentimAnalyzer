import unittest
from sentim_analyzer import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_analyse_sentiment_positif(self):
        # Envoyer une requête POST à l'API avec un texte positif
        response = self.app.post('/analyse_sentiment', json={'text': 'Ceci est un texte positif.'})
        data = response.get_json()

        # Vérifier que la réponse contient le texte et le sentiment
        self.assertIn('texte', data)
        self.assertIn('sentiment', data)

        # Vérifier que le sentiment détecté est positif
        self.assertEqual(data['sentiment'], 'positif')

    def test_analyse_sentiment_negatif(self):
        # Envoyer une requête POST à l'API avec un texte négatif
        response = self.app.post('/analyse_sentiment', json={'text': 'Ceci est un texte négatif.'})
        data = response.get_json()

        # Vérifier que la réponse contient le texte et le sentiment
        self.assertIn('texte', data)
        self.assertIn('sentiment', data)

        # Vérifier que le sentiment détecté est négatif
        self.assertEqual(data['sentiment'], 'négatif')

    def test_analyse_sentiment_neutre(self):
        # Envoyer une requête POST à l'API avec un texte neutre
        response = self.app.post('/analyse_sentiment', json={'text': 'Ceci est un texte neutre.'})
        data = response.get_json()

        # Vérifier que la réponse contient le texte et le sentiment
        self.assertIn('texte', data)
        self.assertIn('sentiment', data)

        # Vérifier que le sentiment détecté est neutre
        self.assertEqual(data['sentiment'], 'neutre')

if __name__ == '__main__':
    unittest.main()
