from django.shortcuts import render

# Create your views here.
def home_screen_views(request):
    print(request.headers)
    return render (request, "personal\home.html", {})
