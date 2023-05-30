from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .forms import RequestForm

# Create your views here.
def index(request):
    return render(request, "services/index.html")

# new request
@login_required
def newRequest(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect(reverse("services:index"))
    else:
        form = RequestForm()
    return render(request, "services/new-request.html", {"form": form})
