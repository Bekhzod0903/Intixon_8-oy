from django.urls import path
from .views import home, income_view, expense_view

urlpatterns = [
    path('', home, name='home'),
    path('income/', income_view, name='income'),
    path('expense/', expense_view, name='expense'),
]
