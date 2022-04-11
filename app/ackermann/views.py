from django.http import JsonResponse
from django.views import View

from app.constants import AckermannConstants


class AckermannView(View):
    """This is function to find the ackermann of an integer.

    :Args:
        number1: Integer positive number.
        number2: Integer positive number.
    :Returns:
        (object):
            {
                'original_input': Original number to get it's ackermann,
                'message': A successful/faliure status msg,
                'result': A number represents the ackermann.
            }
    """

    def get(self, request):
        '''Handles GET requests to calculate ackermann of a num.'''
        number1 = int(request.GET.get('number1'))
        number2 = int(request.GET.get('number2'))
        if number1 <= 0 or number2 <= 0:
            ackermann_num = None
            status_code = 400
            message = AckermannConstants.ACKERMANN_FAILURE
        else:
            message = AckermannConstants.ACKERMANN_SUCCESS
            ackermann_num = self._calculate_ackermann(number1, number2)
            status_code = 200

        data = {
            'original_input': [number1, number2],
            'message': message,
            'result': ackermann_num
        }
        return JsonResponse(data, status=status_code)

    def _calculate_ackermann(self, m, n, s="% s"):
        '''Calculates achermann for two numbers'''
        if m == 0:
            return n + 1
        if n == 0:
            return self._calculate_ackermann(m - 1, 1, s)
        n2 = self._calculate_ackermann(
            m, n - 1, s % ("A(% d, %% s)" % (m - 1)))
        return self._calculate_ackermann(m - 1, n2, s)
