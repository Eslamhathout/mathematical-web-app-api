import json
import unittest

from django.test import Client

from app.constants import FibonacciConstants


class TestFibonacci(unittest.TestCase):
    '''Tests fibonacci API'''

    def setUp(self) -> None:
        self.client = Client()

    def test_fibonacci_positive_number(self):
        '''Test fibonacci function happy scenario'''
        # When: Given a positive number to get fibonacci
        number = 10
        response = self.client.get('/fibonacci/', data={'number': number})
        # Then: we get the fibonacci of the number.
        data = json.loads(response.content)
        self.assertEqual(int(data['original_input']), number)
        self.assertEqual(data['message'], FibonacciConstants.FIBONACCI_SUCCESS)
        self.assertEqual(data['result'], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_negative_number(self):
        '''Test fibonacci function negative num'''
        # When: Given a negative number to get fibonacci
        number = -10
        response = self.client.get('/fibonacci/', data={'number': number})
        # Then: we get the fibonacci of the number.
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(int(data['original_input']), int(number))
        self.assertEqual(data['message'], FibonacciConstants.FIBONACCI_FAILURE)
        self.assertEqual(data['result'], None)


if __name__ == "__main__":
    unittest.main()
