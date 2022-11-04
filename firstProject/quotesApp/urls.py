from django.urls import path
from quotesApp import views as dq

urlpatterns = [
    path('quote', dq.displayQuotes)
]
