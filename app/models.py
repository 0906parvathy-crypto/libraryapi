from django.db import models

# Create your models here.
class Book(models.Model):
    language_mode=(("english","ENGLISH"),
                   ("malayalam","MALAYALAM"),
                   ("hindi","HINDI"))
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    language=models.CharField(max_length=20,choices=language_mode)
    price=models.IntegerField()
    page=models.IntegerField()
    image=models.ImageField(upload_to="Books",null=True)
