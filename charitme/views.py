from django.http import HttpResponse

def home(request):
    return HttpResponse("Charit.me => This is the current HomePage")