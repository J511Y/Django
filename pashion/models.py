from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length = 15, null = False, blank = False)
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    profile_image = models.ImageField(null = True, upload_to = 'images/')
    nickname = models.CharField(max_length = 10)
    description = models.TextField(null = True)

    def __str__(self):
        return self.name + '(' + self.nickname + ')'