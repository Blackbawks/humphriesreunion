"""
Definition of views.
"""

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from crispy_forms.helper import FormHelper
from app.forms import Moms
from app.models import *

import logging
from django.http.response import HttpResponse


logger = logging.getLogger(__name__)


def home(request):
    """Renders the home page."""

    Momsform = Moms()
    people = Person.objects.all()
        
    assert isinstance(request, HttpRequest)
    context = {'Moms':Momsform, 'people':people, 'year':datetime.now().year}
    return render(request, 'app/index.html', context)    


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )




#@csrf_exempt
def dbPostother(request):
    if request.method == 'POST':
#    #if request.is_ajax():
        #dad = Dads(request.POST)
        mom = Moms(request.POST)
        #person = PersonForm(request.POST)
        #if dad.is_valid() and mom.is_valid() and person.is_valid():
        if mom.is_valid():
            #fath = dad.save(commit = False)
            moth = mom.save(commit = False)
            #post = person.save(commit = False)
                        
            fath = Fathers()
            try:
                fath.id = Fathers.objects.all().order_by('-id').values_list()[0][0] + 1
            except:
                fath.id = 1  
            fath.city_of_birth = request.POST['dadscity_of_birth']
            fath.country_of_birth = CitiesCountry.objects.get(code = request.POST['dads_country_of_birth'])
            fath.region_of_birth = request.POST['dadsregion_of_birth']
            fath.first = request.POST['dadsfirst']
            fath.middle = request.POST['dadsmiddle']
            fath.last = request.POST['dadslast']
            fath.year_born = request.POST['dadsyear_of_birth']            
            fath.save()

            try:
                moth.id = Mothers.objects.all().order_by('-id').values_list()[0][0] + 1
            except:
                moth.id = 1  
            moth.city_of_birth = request.POST['momscity_of_birth']
            moth.country_of_birth = CitiesCountry.objects.get(code = request.POST['moms_country_of_birth'])
            moth.region_of_birth = request.POST['momsregion_of_birth']
            moth.first = request.POST['momsfirst']
            moth.middle = request.POST['momsmiddle']
            moth.maiden = request.POST['momsmaiden']
            moth.year_born = request.POST['momsyear_of_birth']            
            moth.save()

            post = Person()
            try:            
                post.id = Person.objects.all().order_by('-id').values_list()[0][0] + 1
            except:
                post.id = 1
            post.family = request.POST.get("LastName","")
            post.first = request.POST.get("FirstName","")
            post.middle = request.POST.get("MiddleName","")
            post.email = request.POST['email']
            post.year_born = request.POST['YearBorn']            
            post.country = CitiesCountry.objects.get(code = request.POST.get("country",""))
            post.region = request.POST.get("CurReg","")
                                             
            post.city = request.POST['CurCity']                        
            post.city_of_birth = request.POST['BirthCity']
            post.region = request.POST['BirthReg']            
            post.country_of_birth = CitiesCountry.objects.get(code = request.POST.get("country_of_birth",""))                        
            post.birth_mother = Mothers.objects.get(pk=moth.id)
            post.birth_father = Fathers.objects.get(pk=fath.id)
            post.place_to_stay = request.POST.get("PlacetoStay","")
            
            
            post.save()


            return HttpResponse('')
        else:
            print dad.errors
            #print mom.errors
            #print person.errors
            context = {'year':datetime.now().year}
            return render(request, 'app/about.html', context)                         
          
#        #moth = Mothers()
#                 





                                  
                
#        #else:
#            #print form.errors                       
           
#    #else:
#    #    form = Information()
    
#    #    args['form'] = form
#    #    return render(request, 'app/index.html', args)
