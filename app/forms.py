from django import forms
from app.constants import SEX, SCIENTIFIC_AREA, POSITION, COMMUNICATION_CHANNELS

SEX_EMPTY = [('','Indique su sexo')] + list(SEX)
SCI_AREA_EMPTY = [('','Indique su área de actuación')] + list(SCIENTIFIC_AREA)
POSITION_EMPTY = [('','Indique su nivel académico')] + list(POSITION)
CHANNEL_EMPTY = [('','Indique un canal de comunicación')] + list(COMMUNICATION_CHANNELS)
BECAL = [(False, 'Es becario BECAL?'), (False, 'No'), (True, 'Si')]


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su nombre'
        }
    ))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su apellido'
        }
    ))
    sex = forms.ChoiceField(label='Sexo', choices=SEX_EMPTY, required=False, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su correo electrónico'
        }
    ))
    has_becal_scholarship = forms.ChoiceField(label='Es becario de BECAL?', choices=BECAL, required=False, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))
    scientific_area = forms.ChoiceField(label='Area de Actuación', choices=SCI_AREA_EMPTY, widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    position = forms.ChoiceField(label='Nivel Académico', choices=POSITION_EMPTY, widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    communication_channel = forms.ChoiceField(label='Canal Comunicación', required=False, choices=CHANNEL_EMPTY,
                                              help_text='Si desea mantener contacto con los investigadores registrados '
                                                        'en este sitio (se utilizará el que elija la mayoría)',
                                              widget=forms.Select(
        attrs={
            'class': 'form-control',
            'onchange': "showPhoneField();"
        }
    ))
    phone_number = forms.CharField(label='', required=False, help_text='',
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Indique su número de teléfono (con código de país)',
                                           'style': 'display:none;'
                                       }
                                   ))
    facebook_profile = forms.URLField(label='', required=False, widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el enlace a su perfil de Facebook',
            'style': 'display:none;'
        }
    ))
    twitter_handler = forms.CharField(label='Usuario de Twitter', help_text='sin @', required=False, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su usuario de Twitter'
        }
    ))
    gscholar_profile = forms.URLField(label='Perfil de Google Scholar', required=False, widget=forms.URLInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el enlance su perfil de Google Scholar'
        }
    ))
    scopus_profile = forms.URLField(label='Perfil de Scopus', required=False, widget=forms.URLInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el enlacen a su perfil de Scopus'
        }
    ))
    personal_website = forms.URLField(label='Página web personal', required=False, widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el enlace a su página web personal'
        }
    ))
    institutional_website = forms.URLField(label='Perfil en web institucional', required=False, widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el enlace a su perfil en la web institucional'
        }
    ))
    orcid = forms.CharField(label='Perfile Orcid', required=False, widget=forms.URLInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el enlace a su perfil Orcid'
        }
    ))
    location_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    location_lat = forms.CharField(widget=forms.HiddenInput(), required=False)
    location_lng = forms.CharField(widget=forms.HiddenInput(), required=False)