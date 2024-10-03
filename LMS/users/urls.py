from django.urls import path
from . import views

# app_name = "users"
urlpatterns = [
    
    path('afaire2/<int:pk>', views.AfaireDetailView.as_view(), name='afaire2'),
    path('classe_list/', views.ClasseListView.as_view(), name='classe_list'),
    path('classe_detail/<int:pk>',
         views.ClasseDetailView.as_view(), name='classe_detail'),
    path('profil_detail/<int:pk>',
         views.ProfilDetailView.as_view(), name='profil_detail')
]
