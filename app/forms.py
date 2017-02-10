"""
Definition of forms.
"""
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import CitiesCity, CitiesCountry, Person, Mothers, Fathers
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Field, Layout, HTML, ButtonHolder
from crispy_forms.bootstrap import InlineCheckboxes, Div, FormActions, AccordionGroup, Accordion, Container, PrependedText, StrictButton, InlineRadios






class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))





class Dads(forms.ModelForm):
    
    dadsfirst = forms.CharField(
         label = "Father's first name"
        )
    dadsmiddle = forms.CharField(
         label = "Father's middle name(s)"
        )
    dadslast = forms.CharField(
         label = "Father's last name"
        )
    dadsregion_of_birth = forms.CharField(
        label = "Which province/region?"
        )
    dadscity_of_birth = forms.CharField(
        label = "What city was he born in?"
        )
    dadsyear_of_birth = forms.IntegerField(
        label = "What year was he born?",
        max_value=2017
    )

    dads_country_of_birth = forms.ModelChoiceField(
        label='What country was he born in?',
        queryset = CitiesCountry.objects.all()
        )


    class Meta:
        model = Fathers
        exclude = ('id',)
        

    def __init__(self, *args, **kwargs):
        super(Dads, self).__init__(*args,**kwargs)        
        self.helper = FormHelper()    
        self.helper.form_class='form-horizontal'
        self.helper.form_id = 'id-information'
        self.helper.form_method = 'post'
        self.helper.form_action = 'dbPostother'
        self.helper.layout = Layout(
            Div(
            HTML('</br>'),
            Fieldset("Father's information",
                'dadsfirst',
                'dadsmiddle',            
                'dadslast',
                'dadsyear_of_birth',
                'dadscity_of_birth',                
                'dadsregion_of_birth',
                'dads_country_of_birth',
                ),
            css_class='col-md-12'
             ),
            Div(
                 FormActions(Submit('dbPostother', 'Save data', css_class='btn btn-success btn-lg', action=".")),
                  css_class = 'col-md-12'
              )            
        )     















 
class Moms(forms.ModelForm):
    
    momsfirst = forms.CharField(
         label = "Mother's first name"
        )
    momsmiddle = forms.CharField(
         label = "Mother's middle name(s)"
        )
    momsmaiden = forms.CharField(
         label = "Mother's maiden name"
        )
    momsregion_of_birth = forms.CharField(
        label = "Which province/region?"
        )
    momscity_of_birth = forms.CharField(
        label = "What city was she born in?"
        )
    momsyear_of_birth = forms.IntegerField(
        label = "What year was she born?",
        max_value=2017
    )

    moms_country_of_birth = forms.ModelChoiceField(
        label='What country was she born in?',
        queryset = CitiesCountry.objects.all()
        )




    dadsfirst = forms.CharField(
         label = "Father's first name"
        )
    dadsmiddle = forms.CharField(
         label = "Father's middle name(s)"
        )
    dadslast = forms.CharField(
         label = "Father's last name"
        )
    dadsregion_of_birth = forms.CharField(
        label = "Which province/region?"
        )
    dadscity_of_birth = forms.CharField(
        label = "What city was he born in?"
        )
    dadsyear_of_birth = forms.IntegerField(
        label = "What year was he born?",
        max_value=2017
    )

    dads_country_of_birth = forms.ModelChoiceField(
        label='What country was he born in?',
        queryset = CitiesCountry.objects.all()
        )
    FirstName = forms.CharField(
        label = "First name",               
        )
    MiddleName = forms.CharField(
        label = "Middle names",      
        )
    LastName = forms.CharField(
        label = "Last name",       
        )
    email = forms.EmailField(
        label = "email address",       
        )
    CurCity = forms.CharField(
        label = "Which city do you live in?",      
        )
    CurReg = forms.CharField(
        label = "Which provice/region?"
        )

    BirthCity = forms.CharField(
        label = "What city were you born in?",
        )
    BirthReg = forms.CharField(
        label = "Which province/region?"
        )

    PlacetoStay = forms.ChoiceField( 
        label = "Do you have a place to stay?",
        choices=(
            (True, u'Yes'),
            (False, u'No'),  
          )
        )
    YearBorn = forms.IntegerField( 
        label = "What year were you born?",
        max_value=2017        
        )

    country = forms.ModelChoiceField(
        label='What country do you live in?',
        queryset = CitiesCountry.objects.all()
        )

    country_of_birth = forms.ModelChoiceField(
        label='What country were you born in?',
        queryset = CitiesCountry.objects.all()
        )

    class Meta:
        model = Mothers
        exclude = ('id',)
        

    def __init__(self, *args, **kwargs):
        super(Moms, self).__init__(*args,**kwargs)        
        self.helper = FormHelper()    
        self.helper.form_class='form-horizontal'
        self.helper.form_id = 'id-information'
        self.helper.form_method = 'post'
        self.helper.form_action = 'dbPostother'
        self.helper.layout = Layout(
            Div(
            Fieldset('',
                'FirstName',
                'MiddleName',            
                'LastName',
                'email',
                'YearBorn',
                'CurCity',
                'CurReg',
                'country',
                'BirthCity',                
                'BirthReg',
                'country_of_birth',
                InlineRadios('PlacetoStay')  

                ),
            css_class='col-md-12'
             ),
            Div(
            HTML('</br>'),
            Fieldset("Mother's information",
                'momsfirst',
                'momsmiddle',            
                'momsmaiden',
                'momsyear_of_birth',
                'momscity_of_birth',                
                'momsregion_of_birth',
                'moms_country_of_birth',
                ),
            css_class='col-md-12'
             ),
            HTML('</br>'),
            Div(          
            Fieldset("Father's information",
                'dadsfirst',
                'dadsmiddle',            
                'dadslast',
                'dadsyear_of_birth',
                'dadscity_of_birth',                
                'dadsregion_of_birth',
                'dads_country_of_birth',
                ),
            css_class='col-md-12'
             ),
            HTML('</br>'),
            Div(
                 FormActions(Submit('dbPostother', 'Save data', css_class='btn btn-success btn-lg', action=".")),
                  css_class = 'col-md-12'
              ),                        
                        
              HTML('<div class="col-md-12" id="savesuccess"></div>')
        )            


 



