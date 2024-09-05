from django.shortcuts import render, HttpResponse

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = render(request, 'myapp/siteuc.html')
        return response