import json
import math
import unittest

from django.test import Client

from app.constants import FactorialConstants


class TestFactorial(unittest.TestCase):
    '''Tests factorial API'''

    def setUp(self) -> None:
        self.client = Client()

    def test_factorial_positive_number(self):
        '''Test factorial function happy scenario'''
        # When: Given a positive number to get factorial
        number = 5
        response = self.client.get('/factorial/', data={'number': number})
        # Then: we get the factorial of the number.
        data = json.loads(response.content)
        self.assertEqual(int(data['original_input']), int(number))
        self.assertEqual(data['message'], FactorialConstants.FACTORIAL_SUCCESS)
        self.assertEqual(int(data['result']), math.factorial(number))

    def test_factorial_negative_number(self):
        '''Test factorial function negative num'''
        # When: Given a negative number to get factorial
        number = -5
        response = self.client.get('/factorial/', data={'number': number})
        # Then: we get the factorial of the number.
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(int(data['original_input']), int(number))
        self.assertEqual(data['message'], FactorialConstants.FACTORIAL_FAILURE)
        self.assertEqual(data['result'], None)


if __name__ == "__main__":
    unittest.main()
