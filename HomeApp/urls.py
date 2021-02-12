from django.urls import path
from HomeApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('whoWeAre/',views.whoWeAre,name="whoWeAre"),
    path('contact/',views.contact,name="contact"),
    path('products/',views.products,name="products"),
    path('resultForm/',views.resultForm,name='resultForm'),
]