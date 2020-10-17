from rest_framework.response import Response
from collections import OrderedDict
import traceback


def custom_exception_handler(exc, content):
    response = Response({
        'success': False,
        'error': exc.__class__.__name__,
        'message': str(exc),
        'details': get_error_details()
    })

    return response


def get_error_details():
    trace = str(traceback.format_exc())
    return OrderedDict(("l{0:02d}".format(n), l) for n, l in enumerate(trace.split('\n'), 1))