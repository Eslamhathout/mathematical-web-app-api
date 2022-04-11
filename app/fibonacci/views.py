from django.http import JsonResponse
from django.views import View

from app.constants import FibonacciConstants


class FibonacciView(View):
    """This is function to find the fibonacci of an integer.

    :Args:
        number: Integer positive number.
    :Returns:
        (object):
            {
                'original_input': Original number to get it's fibonacci,
                'message': A successful/faliure status msg,
                'result': A number represents the fibonacci.
            }
    """

    def get(self, request):
        '''Handles GET requests to calculate fibonacci of a num.'''
        number = int(request.GET.get('number'))
        if number <= 0:
            fibonacci_num = None
            status_code = 400
            message = FibonacciConstants.FIBONACCI_FAILURE
        elif number <= 1:
            fibonacci_num = number
            message = FibonacciConstants.FIBONACCI_SUCCESS
            status_code = 200
        else:
            message = FibonacciConstants.FIBONACCI_SUCCESS
            fibonacci_num = self._calculate_fibonacci(number)
            status_code = 200

        data = {
            'original_input': number,
            'message': message,
            'result': fibonacci_num
        }
        return JsonResponse(data, status=status_code)

    def _calculate_fibonacci(self, number):
        '''Calculates fibonacci of a number.'''
        n1, n2 = 0, 1
        count = 0
        sequesnce = []
        while count < number:
            sequesnce.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return sequesnce
