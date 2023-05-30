from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# service type
class ServiceType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
# services models
class Service(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ServiceType, related_name="type", on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="type", on_delete=models.CASCADE)
