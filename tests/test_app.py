import unittest
import requests


class TestApp(unittest.TestCase):

    def test_predict_endpoint(self):
        # Given
        data = {
            "features": [
                0.00632, 18.0, 2.31, 0.0, 0.538, 6.575, 65.2, 4.0900,
                1.0, 296.0, 15.3, 396.90, 4.98
            ]
        }
        url = "http://localhost:5000/predict"

        # When
        response = requests.post(url, json=data)
        prediction = response.json()["prediction"]

        # Then
        self.assertTrue(isinstance(prediction, list))
        self.assertEqual(len(prediction), 1)


if __name__ == '__main__':
    unittest.main()
