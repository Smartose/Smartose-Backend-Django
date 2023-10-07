from django.http import JsonResponse
import random

def random_data(request):
    data = {
        'message': 'Hello, World!',
        'random_number': random.randint(1, 100)
    }
    return JsonResponse(data)
