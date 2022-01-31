from django.shortcuts import render

from .models import Sentence


def sentences(request):
    return render(request, "sentences/sentences.html")
