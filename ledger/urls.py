from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('list', RecipeListView.as_view(), name='list'),
    path('<int:pk>/info', RecipeDetailView.as_view(), name='recipe-info')
]
app_name = 'ledger'