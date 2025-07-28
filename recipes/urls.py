from django.urls import path
from recipes.views import home, contato, sobre

    
    # return HTTP Response

urlpatterns = [
    path('', home),
    path('sobre/', sobre), # /sobre/
    path('contato/', contato) # /contato/
]