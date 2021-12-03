from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name="acceuil"),
    path('produit/',views.product,name="produit"),
    path('about/',views.about,name="about"),
]