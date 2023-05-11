from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.views import generic
from .models import Sisestatav
from .models import Tulemus
from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#class SisestaView(generic.DetailView):
    #template_name = 'kulutustekalkulaator/sisestatav.html'
    #model = Sisestatav
    #def get_queryset(self):
        #return Sisestatav.objects.all()

#class TabelView1(generic.DetailView):
    #template_name = 'kulutustekalkulaator/tabel.html'
    #context_object_name = 'tabellist'
    #def get_queryset(self):
        #return Sisestatav.objects.all()
class SisestusedForm(forms.Form):
    nimi_b = forms.CharField(label="nimi_b", max_length=50)
    summa = forms.DecimalField(label="summa", max_digits = 5, decimal_places = 2)
    info = forms.CharField(label="info", max_length=100)




def TabelView(request):
  if request.method == "POST":
      form = SisestusedForm(request.POST)
      if form.is_valid():
          sis = Sisestatav(võlgneja=request.user.username, #Siia saab asemele panna user.first_name kui on soov
                              makstav=form.cleaned_data["nimi_b"],
                              väärtus=form.cleaned_data["summa"],
                              kirjeldus=form.cleaned_data["info"]
                              )
          sis.save()



  sise = Sisestatav.objects.all().values()

  sise2 = Tulemus.objects.raw("select ROW_NUMBER() OVER ( ORDER BY `võlgneja` ) as id, `võlgneja` as nimi, sum(`väärtus`) as `väärtus` from ( select `võlgneja`, -`väärtus` as `väärtus` from kulutustekalkulaator_sisestatav union ALL select `makstav` as `võlgneja`, `väärtus` from kulutustekalkulaator_sisestatav ) as A group by `võlgneja`")
  #Siin saaks filtreerida useri kaudu, aga mu isa arvates sobis see ikka ülesandega kokku

  template = loader.get_template('tabel_all.html')
  context = {
    'sise': sise,
    'sise2': sise2,
  }
  return HttpResponse(template.render(context, request))