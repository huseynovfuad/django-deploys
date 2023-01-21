from django.shortcuts import render, HttpResponse
from .tasks import test_task
from datetime import datetime, timedelta

# Create your views here.


def index_view(request):
    tomorrow = datetime.now() + timedelta(minutes=1)
    test_task.apply_async((), eta=tomorrow)
    return HttpResponse("hello world")