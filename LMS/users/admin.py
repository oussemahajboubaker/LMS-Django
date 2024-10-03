from django.contrib import admin
from .models import Note, Question, Reponse, Classe, Profil

# Register your models here.


class adminNote(admin.ModelAdmin):
    fields = ('user', 'test1', 'test2', 'test3')


class adminQuestion(admin.ModelAdmin):
    fields = ['champ_question', 'classe']


admin.site.register(Note, adminNote)
admin.site.register(Question, adminQuestion)
admin.site.register(Reponse)
admin.site.register(Classe)
admin.site.register(Profil)