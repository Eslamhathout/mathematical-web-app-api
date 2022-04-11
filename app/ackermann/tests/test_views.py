import json
import unittest

from django.test import Client

from app.constants import AckermannConstants


class Testackermann(unittest.TestCase):
    '''Tests ackermann API'''

    def setUp(self) -> None:
        self.client = Client()

    def test_ackermann_positive_number(self):
        '''Test ackermann function happy scenario'''
        # When: Given a positive number to get ackermann
        number1 = 2
        number2 = 3
        response = self.client.get(
            '/ackermann/', data={'number1': number1, 'number2': number2})
        # Then: we get the ackermann of the number.
        data = json.loads(response.content)
        self.assertEqual(data['original_input'], [number1, number2])
        self.assertEqual(data['message'], AckermannConstants.ACKERMANN_SUCCESS)
        self.assertEqual(int(data['result']), 9)

    def test_ackermann_negative_number(self):
        '''Test ackermann function negative num'''
        # When: Given a negative number to get ackermann
        number1 = -5
        number2 = 5
        response = self.client.get(
            '/ackermann/', data={'number1': number1, 'number2': number2})
        # Then: we get the ackermann of the number.
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['original_input'], [number1, number2])
        self.assertEqual(data['message'], AckermannConstants.ACKERMANN_FAILURE)
        self.assertEqual(data['result'], None)


if __name__ == "__main__":
    unittest.main()
