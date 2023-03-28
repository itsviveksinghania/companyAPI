# Views can be function based and class based
from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page request")
    friends = ['vivek', 'poo', 'ronaldo']
    return JsonResponse(friends, safe=False)
