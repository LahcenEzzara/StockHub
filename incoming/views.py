from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def incoming(request):
    return render(request, 'incoming/index.html')


@login_required
def new(request):
    return render(request, 'incoming/new.html')


@login_required
def graph(request):
    return render(request, 'incoming/graph.html')
