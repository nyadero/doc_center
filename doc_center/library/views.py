from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Category, Document

from .forms import NewDocumentForm, LendDocument

# Create your views here.

# index
def index(request):
    # find all documents
    documents = Document.objects.all().order_by("created_at")
    # categories
    categories = Category.objects.all()
    return render(request, "library/index.html", {"documents": documents, "categories": categories})

# search documents
def documentsByCategory(request):
    if request.method == "GET":
        query = request.GET.get("search")
        searchRequest = request.GET.get("search")
        if query is not None:
            lookup = Q(name__icontains = query) | Q(issued_to__icontains = query) | Q(description__icontains = query)
            documents = Document.objects.filter(lookup).distinct()
            # category = Document.objects.filter(categories=Category.objects.get())
            return render(request, "library/index.html", {"query": query, "documents": documents, "searchRequest": searchRequest})
        else:
            return render(request, "library/index.html")  
    else:
        return render(request, "library/index.html")

# new document
@login_required
def newDocument(request):
    if request.method == "POST":
        form = NewDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document= form.save(commit=False)
            document.created_by = request.user
            document.save()
            return redirect("library:index")
    else:
        form = NewDocumentForm()
    return render(request, "library/new-document.html", {"form": form})


# document by id
def singleDocument(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, "library/document.html", {'document': document})

# update document
@login_required
def updateDocument(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        form = NewDocumentForm(instance=document, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("library:index")
    else:
        form = NewDocumentForm(instance=document)
    return render(request, "library/edit-document.html", {"form": form, "object": document})


# delete document
@login_required
def deleteDocument(request, pk):
    document_object = get_object_or_404(Document, pk=pk)
    document_object.delete()
    return redirect(reverse("library:index"))

# issue book only when the column borrowed is false
@login_required
def issueDocument(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        form = LendDocument(instance=document, data=request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.issued_to = request.POST.get("issued_to")
            document.borrowed = True
            document.issued_by = request.user.username
            document.save()
            return redirect("library:index")
    else:
        form = LendDocument(instance=document)
    return render(request, "library/issue-document.html", {"form": form, "object": document})

# mark borrowed books as returned
def returnDocument(request, pk):
    document_object = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        checked = request.POST.get("borrowed")
        if checked:
            document = document_object.save(commit=False)
            document.borrowed = False
            document.save()
        else:
            document = document_object.save(commit=False)
            document.borrowed =True
            document.save()
    render(request, "library/index.html", {"checked" : checked})