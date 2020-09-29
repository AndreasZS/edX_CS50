import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    dt_now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": (dt_now.month == 1 and dt_now.day == 1)
    })