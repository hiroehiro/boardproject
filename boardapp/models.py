from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100)
    images=models.ImageField(upload_to="")
    good=models.IntegerField()
    read=models.IntegerField() #既読した人数
    readtext=models.CharField(max_length=200) #既読した人の名前を保管
    