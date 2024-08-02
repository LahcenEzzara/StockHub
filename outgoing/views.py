from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def outgoing(request):
    return render(request, 'outgoing/index.html')


@login_required
def new(request):
    return render(request, 'outgoing/new.html')


@login_required
def graph(request):
    return render(request, 'outgoing/graph.html')