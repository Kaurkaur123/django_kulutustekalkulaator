from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #path('', views.TabelView.as_view(), name='tabel')
    path('', views.TabelView, name='tabel')
]