from django.shortcuts import render

# Create your views here.
def book(request):

    return render(request, 'book.html')

def video(request):

    return render(request, 'videos.html')


def movie(request):

    return render(request, 'movies.html')


