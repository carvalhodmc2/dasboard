from django.shortcuts import render


def index(request):
    """ Index Page """

    template = 'pages/index.html'
    context = {}

    return render(request, template, context)
