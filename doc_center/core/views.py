from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from library.models import Document, Category

# Create your views here.

# logged in user dashboard
@login_required
def index(request):
    categories = Category.objects.filter().all()
    borrowed = Document.objects.filter(borrowed = True).all()
    return render(request, "core/index.html", {"categories": categories, "borrowed": borrowed})


# logout user
def logout_user(request):
    logout(request)
    return redirect("library:index")
