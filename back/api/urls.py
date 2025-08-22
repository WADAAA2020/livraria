from django.urls import path
from .views import AutoresView, listar_autores, EditorasView, LivrosView

urlpatterns = [
    path('autores', AutoresView.as_view()),
    path('authors', listar_autores),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),
]
