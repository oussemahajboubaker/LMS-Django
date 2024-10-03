from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfilUpdateForm, ReponseForm
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import user_passes_test
from django.views import generic
from .models import Note, Question, Reponse, Profil, Classe
import matplotlib.pyplot as plt
import io
from django.core.files.images import ImageFile
import urllib
import base64
import numpy as np
import plotly.offline as opy
import plotly.graph_objs as go
from .forms import ReponseForm
from django.views.generic import DetailView

# Create your views here.


def home(request):
    #TODO
    return render(request, 'users\home.html')


@login_required
def profil(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profil mis à jour avec succès !')
            return redirect('profil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profil)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profil.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def resultas(request):
    
    prof = Profil.objects.filter(user=User.objects.get(username=request.user)).first()
    curr = Note.objects.filter(user=prof.user).first()


    l = eval(curr.test1)
    plt.clf()
    data = {'MATH': l[0], 'PHY': l[1], 'PY': l[2], 'RA': l[3], 'PROG': l[4]}
    cours = list(data.keys())
    valeurs = list(data.values())
    
    figure = io.BytesIO()
    fig = plt.subplots(figsize=(6, 6))
    plt.bar(cours, valeurs, color='maroon', width=0.4)
    plt.xlabel("Cours")
    plt.ylabel("Points")
    plt.title("Scores Test 1")
    plt.savefig(figure, format="png")
    content_file = ImageFile(figure)
    curr.testplot1.save('testplot1.png', content_file)
    plt.clf()

    l1 = eval(curr.test2)
    #TODO afficher testplot2
    plt.clf()
    data = {'MATH': l1[0], 'PHY': l1[1], 'PY': l1[2], 'RA': l1[3], 'PROG': l1[4]}
    cours = list(data.keys())
  
    valeurs1 = list(data.values())
    
    figure = io.BytesIO()
    fig = plt.subplots(figsize=(6, 6))
    plt.bar(cours, valeurs1, color='maroon', width=0.4)
    plt.xlabel("Cours")
    plt.ylabel("Points")
    plt.title("Scores Test 2")
    plt.savefig(figure, format="png")
    content_file = ImageFile(figure)
    curr.testplot2.save('testplot2.png', content_file)
    plt.clf()
    
    
    
    l2 = eval(curr.test3)
    #TODO afficher testplot3
    plt.clf()
    data = {'MATH': l2[0], 'PHY': l2[1], 'PY': l2[2], 'RA': l2[3], 'PROG': l2[4]}
    cours = list(data.keys())
    
    valeurs2 = list(data.values())
    figure = io.BytesIO()
    fig = plt.subplots(figsize=(6, 6))
    plt.bar(cours, valeurs, color='maroon', width=0.4)
    plt.xlabel("Cours")
    plt.ylabel("Points")
    plt.title("Scores Test 3")
    plt.savefig(figure, format="png")
    content_file = ImageFile(figure)
    curr.testplot3.save('testplot3.png', content_file)
    plt.clf()





    figure.seek(0)
    figure.truncate(0)
    fig = plt.subplots(figsize=(6, 6))
    plt.pie(valeurs, labels=cours)
    plt.title("Scores Test 1")
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot4.save('testplot4.png', content_file2)
    plt.clf()

    #TODO afficher testplot5
    figure.seek(0)
    figure.truncate(0)
    fig = plt.subplots(figsize=(6, 6))
    plt.pie(valeurs1, labels=cours)
    plt.title("Scores Test 2")
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot5.save('testplot5.png', content_file2)
    plt.clf()


    

    #TODO afficher testplot6
    figure.seek(0)
    figure.truncate(0)
    fig = plt.subplots(figsize=(6, 6))
    plt.pie(valeurs2, labels=cours)
    plt.title("Scores Test 3")
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot6.save('testplot6.png', content_file2)
    plt.clf()
    
    
    


    figure.seek(0)
    figure.truncate(0)
    barWidth = 1
    fig = plt.subplots(figsize=(12, 8))

    longueur = [6, 12, 18, 24, 30]
    plt.bar([i for i in longueur], valeurs, color='maroon', width=barWidth,
            edgecolor='grey', label='Test 1')
    plt.bar([i+1 for i in longueur], valeurs1, color='grey', width=barWidth,
            edgecolor='grey', label='Test 2')
    plt.bar([i+2 for i in longueur], valeurs2, color='navy', width=barWidth,
            edgecolor='grey', label='Test 3')

    plt.xlabel('Matière', fontweight='bold')
    plt.ylabel('Score', fontweight='bold')
    plt.title("Comparaison des performances")
    plt.xticks([i+1 for i in longueur],
               ['MATH', 'PHY', 'PY', 'RA', 'PROG'])
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot7.save('testplot7.png', content_file2)
    plt.clf()

    trace1 = go.Bar(x=cours, y=valeurs, marker={'color': 'blue'},
                    name='Premier tracé')
    data_plotly = go.Data([trace1])
    layout_plotly = go.Layout(title="Niveau de progression", xaxis={
        'title': 'Score'}, yaxis={'title': 'Matière'})

    figure_plotly = go.Figure(data=data_plotly, layout=layout_plotly)
    div = opy.plot(figure_plotly, auto_open=False, output_type='div')




    #TODO Afficher d'autres statistiques
    figure.seek(0)
    figure.truncate(0)
    barWidth = 1
    fig = plt.subplots(figsize=(12, 8))

    longueur = [6, 12, 18, 24, 30]
    plt.bar([i for i in longueur], valeurs, color='maroon', width=barWidth,
            edgecolor='grey', label='Test 1')
    plt.bar([i+1 for i in longueur], valeurs1, color='grey', width=barWidth,
            edgecolor='grey', label='Test 2')
    plt.bar([i+2 for i in longueur], valeurs2, color='navy', width=barWidth,
            edgecolor='grey', label='Test 3')

    plt.xlabel('Matière', fontweight='bold')
    plt.ylabel('Score', fontweight='bold')
    plt.title("Comparaison des performances")
    plt.xticks([i+1 for i in longueur],
               ['MATH', 'PHY', 'PY', 'RA', 'PROG'])
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot8.save('testplot8.png', content_file2)
    plt.clf()

    trace2 = go.Bar(x=cours, y=valeurs, marker={'color': 'blue'},
                    name='Premier tracé')
    data_plotly = go.Data([trace2])
    layout_plotly = go.Layout(title="Niveau de progression", xaxis={
        'title': 'Score'}, yaxis={'title': 'Matière'})

    figure_plotly = go.Figure(data=data_plotly, layout=layout_plotly)
    div = opy.plot(figure_plotly, auto_open=False, output_type='div')
    
    
    
    
    
    figure.seek(0)
    figure.truncate(0)
    barWidth = 1
    fig = plt.subplots(figsize=(12, 8))

    longueur = [6, 12, 18, 24, 30]
    plt.bar([i for i in longueur], valeurs, color='maroon', width=barWidth,
            edgecolor='grey', label='Test 1')
    plt.bar([i+1 for i in longueur], valeurs1, color='grey', width=barWidth,
            edgecolor='grey', label='Test 2')
    plt.bar([i+2 for i in longueur], valeurs2, color='navy', width=barWidth,
            edgecolor='grey', label='Test 3')

    plt.xlabel('Matière', fontweight='bold')
    plt.ylabel('Score', fontweight='bold')
    plt.title("Comparaison des performances")
    plt.xticks([i+1 for i in longueur],
               ['MATH', 'PHY', 'PY', 'RA', 'PROG'])
    plt.legend()
    plt.savefig(figure, format="png")
    content_file2 = ImageFile(figure)
    curr.testplot9.save('testplot9.png', content_file2)
    plt.clf()

    trace3 = go.Bar(x=cours, y=valeurs, marker={'color': 'blue'},
                    name='Premier tracé')
    data_plotly = go.Data([trace3])
    layout_plotly = go.Layout(title="Niveau de progression", xaxis={
        'title': 'Score'}, yaxis={'title': 'Matière'})

    figure_plotly = go.Figure(data=data_plotly, layout=layout_plotly)
    div = opy.plot(figure_plotly, auto_open=False, output_type='div')
    
    
    
    

    context = {
    'bar': div,
    'images': [
        curr.testplot1.url if curr.testplot1 else None,
        curr.testplot2.url if curr.testplot2 else None,
        curr.testplot3.url if curr.testplot3 else None,
        curr.testplot4.url if curr.testplot4 else None,
        curr.testplot5.url if curr.testplot5 else None,
        curr.testplot6.url if curr.testplot6 else None,
        curr.testplot7.url if curr.testplot7 else None,
    ]
}
    return render(request, 'users/resultas.html', context)



class ClasseListView(generic.ListView):
    model = Classe


class ClasseDetailView(generic.DetailView):
    model = Classe

    def get_context_data(self, **kwargs):
        context = super(ClasseDetailView, self).get_context_data(**kwargs)
        profils = Profil.objects.filter(classe=self.kwargs['pk'])
        context['profils'] = profils
        return context


class ProfilDetailView(generic.DetailView):
    model = Profil

    def get_context_data(self, **kwargs):
        context = super(ProfilDetailView, self).get_context_data(**kwargs)
        reponses = Reponse.objects.filter(
            user=Profil.objects.get(id=self.kwargs['pk']))
        # questions = Question.objects.filter(
        #     classe=Profile.objects.get(id=self.kwargs['pk']).classe)
        # context['questions'] = questions
        context['reponses'] = reponses

        return context


class AfaireDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupère l'id du profil de l'utilisateur connecté
        profil = Profil.objects.get(user=self.request.user)

        # Récupère toutes les questions de la classe du profil, triées par 'id'
        questions = list(Question.objects.filter(classe=profil.classe).order_by('id'))

        # Trouver l'index de la question actuelle basé sur 'pk'
        current_question_id = int(self.kwargs['pk'])
        current_question = Question.objects.get(id=current_question_id)
        current_question_index = questions.index(current_question)

        # Gestion de la réponse précédente (si pas la première question)
        if current_question_index > 0:
            previous_question = questions[current_question_index - 1]
            champ_reponse = self.request.GET.get('champ_reponse', '')
            if champ_reponse:  # Vérifie qu'une réponse est bien soumise
                Reponse.objects.create(
                    question=previous_question,
                    champ_reponse=champ_reponse,
                    user=profil.user
                )

        # Déterminer si la question actuelle est la dernière
        if current_question_index + 1 == len(questions):
            context['end'] = True
        else:
            context['button'] = "Suivant"

        # Préparer le formulaire de réponse pour la question actuelle
        reponse_form = ReponseForm()
        context['question'] = current_question
        context['reponse'] = reponse_form
        context['index'] = current_question_index + 1

        return context
