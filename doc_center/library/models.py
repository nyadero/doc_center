from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# category for the documents e.g books, reports, 
class Category(models.Model):
    name=models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
# documents
class Document(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ForeignKey(Category, related_name="documents", on_delete=models.CASCADE)
    issued_to = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="document_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    borrowed = models.BooleanField(default=False)
    issued_by = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User, related_name="documents", on_delete=models.CASCADE)
    return_date = models.DateField(null=True)

