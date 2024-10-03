from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classe = models.ForeignKey(
        "classe", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profil_img')
    bio = models.CharField(max_length=2000, blank=True)
    competence = models.CharField(max_length=2000, blank=True)
    github = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Profil de {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Note(models.Model):
    #TODO
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    test1 = models.CharField(max_length=20)
    test2 = models.CharField(max_length=20)
    test3 = models.CharField(max_length=20)
    testplot1 = models.ImageField()
    testplot2 = models.ImageField()
    testplot3 = models.ImageField()
    testplot4 = models.ImageField()
    testplot5 = models.ImageField()
    testplot6 = models.ImageField()
    testplot7 = models.ImageField()
    testplot8 = models.ImageField()
    testplot9 = models.ImageField()
    

class Classe(models.Model):
    #TODO
    classe = models.CharField(max_length=20)
    def __str__(self):
        return self.classe


class Question(models.Model):
    #TODO
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    champ_question = models.CharField(max_length=20)
    def __str__(self):
        return self.champ_question


class Reponse(models.Model):
    #TODO
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    champ_reponse = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return f"{self.user} a répondu {self.champ_reponse}"
    
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)


