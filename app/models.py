from django.db import models

# Create your models here.
class Movie(models.Model) :
    title = models.CharField(max_length=100),
    content = models.TextField(),
    good = models.IntegerField(),
    bad = models.IntegerField(),

class User(models.Model) :
    nickname = models.CharField(max_length=50),

//추가 모델
