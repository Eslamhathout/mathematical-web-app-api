from django.http import JsonResponse
from django.views import View

from app.constants import FactorialConstants


class FactorialView(View):
    """This is a recursive function to find the factorial of an integer.

    :Args:
        number: Integer positive number.
    :Returns:
        (object):
            {
                'original_input': Original number to get it's factorial,
                'message': A successful/faliure status msg,
                'result': A number represents the factorial.
            }
    """

    def get(self, request):
        '''Handles GET requests to calculate factorial of a num.'''
        number = int(request.GET.get('number'))
        if number <= 0:
            factorial_num = None
            status_code = 400
            message = FactorialConstants.FACTORIAL_FAILURE
        elif number == 1:
            factorial_num = 1
            message = FactorialConstants.FACTORIAL_SUCCESS
            status_code = 200
        else:
            message = FactorialConstants.FACTORIAL_SUCCESS
            factorial_num = self._calculate_factorial(number)
            status_code = 200

        data = {
            'original_input': number,
            'message': message,
            'result': factorial_num
        }
        return JsonResponse(data, status=status_code)

    def _calculate_factorial(self, number):
        '''Calculates facorial of a number.'''
        if number == 1:
            return 1
        else:
            return (number * self._calculate_factorial(number-1))
