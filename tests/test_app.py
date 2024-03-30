import unittest
import requests

class TestApp(unittest.TestCase):
    def test_predict_endpoint(self):
        data = {"features": [0.00632, 18.0, 2.31, 0.0, 0.538, 6.575, 65.2, 4.0900, 1.0, 296.0, 15.3, 396.90, 4.98]}
        response = requests.post("http://localhost:5000/predict", json=data)
        prediction = response.json()["prediction"]
        self.assertTrue(isinstance(prediction, list))
        self.assertEqual(len(prediction), 1)
