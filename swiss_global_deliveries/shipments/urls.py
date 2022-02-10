from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import ClientDetailView, ClientListView,ClientCreateView

from . import views

urlpatterns = [
    path("", ClientListView.as_view(), name="home"),
    path("Client/<int:pk/", ClientDetailView.as_view(), name="Client_details"),
    path("pages/", ClientCreateView.as_view(), name="Client_create"),

   
] 



admin.site.site_header = "Administration"
admin.site.site_title = "Swiss Global Deliveries Administration"
admin.site.index_title = "Swiss Global Deliveries"
